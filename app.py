import os

# Ensure Django settings are configured for WSGI
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

from django.core.wsgi import get_wsgi_application

# Expose WSGI app as `app` for gunicorn's default pattern: `gunicorn app:app`
app = get_wsgi_application() 