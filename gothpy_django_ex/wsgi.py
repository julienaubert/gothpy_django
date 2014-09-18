import os
import sys
sys.path.insert(0, os.path.expanduser('~/etc/gothpy_django_ex'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gothpy_django_ex.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
