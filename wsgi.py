from project import app as application

if __name__ == "__main__":
    application.run()


# backup passenger_wsgi
# import imp
# import os
# import sys
#
#
# sys.path.insert(0, os.path.dirname(__file__))
#
# wsgi = imp.load_source('wsgi', 'wsgi.py')
# application = wsgi.application
