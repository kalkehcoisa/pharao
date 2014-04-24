from pyramid.paster import get_app, setup_logging
ini_path = '/var/www/pharao/pharao/production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
