#-*- coding: utf-8 -*-

import sqlalchemy

class Postgresql():
    engine = None
    connection = None

    db_name = 'postgres'
    db_user = 'pharao'
    db_pass = '1234'
    db_host = 'localhost'

    def __init__(self, *args, **kw):
        self.engine = sqlalchemy.create_engine('postgresql://%s:%s@%s/%s' % 
                        (self.db_user, self.db_pass, self.db_host, self.db_name))
        self.connection = self.engine.connect()

    def close(self):
        if self.engine:
            self.engine.dispose()
        if self.connection:
            self.connection.close()

    def connect(self, user=None, passwd=None, host=None, dbname=None):
        self.close()

        self.db_user = user or self.db_user
        self.db_pass = passwd or self.db_pass
        self.db_host = host or self.db_host
        self.db_name = dbname or self.db_name

        self.engine = sqlalchemy.create_engine('postgresql://%s:%s@%s/%s' % 
                        (self.db_user, self.db_pass, self.db_host, self.db_name))
        self.connection = self.engine.connect()


    def databases(self):
        query = "SELECT * FROM pg_database WHERE datistemplate = False;"
        return [p for p in self.connection.execute(query).fetchall()]


    #Postgresql only list the schemas of the current database you're connected to
    def schemas(self, database=None):
        if database:
            self.connect(dbname=database)
        query = """SELECT pn.nspname, pu.usename AS nspowner, pg_catalog.obj_description(pn.oid, 'pg_namespace') AS nspcomment
                  FROM pg_catalog.pg_namespace pn LEFT JOIN pg_catalog.pg_user pu ON (pn.nspowner = pu.usesysid)
                  WHERE pn.nspname NOT LIKE 'pg@_%%' ESCAPE '@' ORDER BY nspname"""
        return [p for p in self.connection.execute(query).fetchall()]

    #Postgresql only list the tables of the current database you're connected to
    def tables(self, all=False, database=None, schema=None):
        if database:
            self.connect(dbname=database)

        where_schema = "AND tb.table_schema = '%s'"%schema if schema else ""
        where = "AND tb.table_schema NOT LIKE 'pg@_%%' ESCAPE '@' " if not all else ""

        query = """SELECT tb.table_catalog, tb.table_schema, tb.table_name
                   FROM information_schema.tables tb
                   WHERE tb.table_schema != 'information_schema'
                    """+where+"""
                    """+where_schema+"""
                ORDER BY tb.table_schema, tb.table_name"""

        return [p for p in self.connection.execute(query).fetchall()]



    '''
    def triggers(self, tablename):
        query = """SELECT
                t.tgname, pg_catalog.pg_get_triggerdef(t.oid) AS tgdef,
                CASE WHEN t.tgenabled = 'D' THEN FALSE ELSE TRUE END AS tgenabled, p.oid AS prooid,
                p.proname || ' (' || pg_catalog.oidvectortypes(p.proargtypes) || ')' AS proproto,
                ns.nspname AS pronamespace
            FROM pg_catalog.pg_trigger t, pg_catalog.pg_proc p, pg_catalog.pg_namespace ns
            WHERE t.tgrelid = (SELECT oid FROM pg_catalog.pg_class WHERE relname='{$table}'
                AND relnamespace=(SELECT oid FROM pg_catalog.pg_namespace WHERE nspname='{$this->_schema}'))
                AND (NOT tgisconstraint OR NOT EXISTS
                        (SELECT 1 FROM pg_catalog.pg_depend d    JOIN pg_catalog.pg_constraint c
                            ON (d.refclassid = c.tableoid AND d.refobjid = c.oid)
                        WHERE d.classid = t.tableoid AND d.objid = t.oid AND d.deptype = 'i' AND c.contype = 'f'))
                AND p.oid=t.tgfoid
                AND p.pronamespace = ns.oid"""
        return [p for p in self.connection.execute(query).fetchall()]


    // Tablespace functions

    /**
     * Retrieves information for all tablespaces
     * @param $all Include all tablespaces (necessary when moving objects back to the default space)
     * @return A recordset
     */
    function getTablespaces($all = false) {
        global $conf;

        $sql = "SELECT spcname, pg_catalog.pg_get_userbyid(spcowner) AS spcowner, spclocation,
                    (SELECT description FROM pg_catalog.pg_shdescription pd WHERE pg_tablespace.oid=pd.objoid) AS spccomment
                    FROM pg_catalog.pg_tablespace";

        if (!$conf['show_system'] && !$all) {
            $sql .= " WHERE spcname NOT LIKE 'pg\\\\_%'";
        }

        $sql .= " ORDER BY spcname";

        return $this->selectSet($sql);
    }

    /**
     * Retrieves a tablespace's information
     * @return A recordset
     */
    function getTablespace($spcname) {
        $this->clean($spcname);

        $sql = "SELECT spcname, pg_catalog.pg_get_userbyid(spcowner) AS spcowner, spclocation,
                    (SELECT description FROM pg_catalog.pg_shdescription pd WHERE pg_tablespace.oid=pd.objoid) AS spccomment
                    FROM pg_catalog.pg_tablespace WHERE spcname='{$spcname}'";

        return $this->selectSet($sql);
    }

    // Constraints methods

    /**
     * Returns a list of all constraints on a table,
     * including constraint name, definition, related col and referenced namespace,
     * table and col if needed
     * @param $table the table where we are looking for fk
     * @return a recordset
     */
    function getConstraintsWithFields($table) {
        global $data;

        $data->clean($table);

        // get the max number of col used in a constraint for the table
        $sql = "SELECT DISTINCT
                max(SUBSTRING(array_dims(c.conkey) FROM  E'^\\\[.*:(.*)\\\]$')) as nb
        FROM
              pg_catalog.pg_constraint AS c
          JOIN pg_catalog.pg_class AS r ON (c.conrelid = r.oid)
              JOIN pg_catalog.pg_namespace AS ns ON r.relnamespace=ns.oid
        WHERE
            r.relname = '$table' AND ns.nspname='". $this->_schema ."'";

        $rs = $this->selectSet($sql);

        if ($rs->EOF) $max_col = 0;
        else $max_col = $rs->fields['nb'];

        $sql = '
            SELECT
                c.contype, c.conname, pg_catalog.pg_get_constraintdef(c.oid, true) AS consrc,
                ns1.nspname as p_schema, r1.relname as p_table, ns2.nspname as f_schema,
                r2.relname as f_table, f1.attname as p_field, f2.attname as f_field,
                pg_catalog.obj_description(c.oid, \'pg_constraint\') AS constcomment
            FROM
                pg_catalog.pg_constraint AS c
                JOIN pg_catalog.pg_class AS r1 ON (c.conrelid=r1.oid)
                JOIN pg_catalog.pg_attribute AS f1 ON (f1.attrelid=r1.oid AND (f1.attnum=c.conkey[1]';
        for ($i = 2; $i <= $rs->fields['nb']; $i++) {
            $sql.= " OR f1.attnum=c.conkey[$i]";
        }
        $sql.= '))
                JOIN pg_catalog.pg_namespace AS ns1 ON r1.relnamespace=ns1.oid
                LEFT JOIN (
                    pg_catalog.pg_class AS r2 JOIN pg_catalog.pg_namespace AS ns2 ON (r2.relnamespace=ns2.oid)
                ) ON (c.confrelid=r2.oid)
                LEFT JOIN pg_catalog.pg_attribute AS f2 ON
                    (f2.attrelid=r2.oid AND ((c.confkey[1]=f2.attnum AND c.conkey[1]=f1.attnum)';
        for ($i = 2; $i <= $rs->fields['nb']; $i++)
            $sql.= "OR (c.confkey[$i]=f2.attnum AND c.conkey[$i]=f1.attnum)";

        $sql .= sprintf("))
            WHERE
                r1.relname = '%s' AND ns1.nspname='%s'
            ORDER BY 1", $table, $this->_schema);

        return $this->selectSet($sql);
    }
'''

