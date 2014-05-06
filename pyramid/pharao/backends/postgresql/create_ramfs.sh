#!/bin/sh
set -e

### BEGIN INIT INFO
# Provides:             postgresql
# Required-Start:       $local_fs $remote_fs $network $time
# Required-Stop:        $local_fs $remote_fs $network $time
# Should-Start:         $syslog
# Should-Stop:          $syslog
# Default-Start:        2 3 4 5
# Default-Stop:         0 1 6
# Short-Description:    PostgreSQL RDBMS server
### END INIT INFO

export PGHOST=${PGHOST-localhost}
export PGPORT=${PGPORT-5432}
export PGDATABASE=${PGDATABASE-pharao}
export PGUSER=${PGUSER-postgres}
export PGPASSWORD=${PGPASSWORD-asdfgh01}

#monta o servidor de testes 
mkdir -p /mnt/ramfs
mkdir -p /mnt/ramfs/pgdata
if ! mount | grep /mnt/ramfs/pgdata > /dev/null; then
    mount -t ramfs none /mnt/ramfs/pgdata
    chown postgres:postgres /mnt/ramfs/pgdata
fi
chmod go-rwx /mnt/ramfs/pgdata

#DUMPFILE=~/dump-$(date +%y-%m-%d).sql
#pg_dump --create --host=localhost -U postgres pharao --schema-only --file=$DUMPFILE 

psql -U postgres --host localhost -c "DROP DATABASE pharao_test;";
psql -U postgres --host localhost -c "DROP TABLESPACE pharao_test;";
psql -U postgres --host localhost -c "CREATE TABLESPACE pharao_test OWNER postgres LOCATION '/mnt/ramfs/pgdata'";
psql -U postgres --host localhost -c "CREATE DATABASE pharao_test WITH OWNER = pharao TABLESPACE = pharao_test;"
psql -U postgres pharao_test --host localhost -c "CREATE EXTENSION hstore;"

#parte comentada para parar com o carregamento do dump, para que o sistema de testes crie as tabelas
#sed -i 's/CREATE DATABASE pharao/CREATE DATABASE pharao_test/g' $DUMPFILE
#sed -i 's/ALTER DATABASE pharao/ALTER DATABASE pharao_test/g' $DUMPFILE
#sed -i "s/'en_US.UTF-8';/'en_US.UTF-8' TABLESPACE=pharao_test;/g" $DUMPFILE
#sed -i 's/connect pharao/connect pharao_test/g' $DUMPFILE

#psql --file=$DUMPFILE -U postgres --host localhost

#/etc/init.d/postgresql restart
