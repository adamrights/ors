import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'ORS.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
path = '/home/adam/.virtualenvs/ors'
if path not in sys.path:
    sys.path.append(path)

path2 = '/home/adam/.virtualenvs/ors/ORS'
if path2 not in sys.path:
    sys.path.append(path2)
