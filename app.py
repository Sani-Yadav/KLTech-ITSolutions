import os
import sys

# Ensure Python can import the inner project package when running from repo root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, "myproject")
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# Ensure Django settings are configured for WSGI
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

from django.core.wsgi import get_wsgi_application

# Expose WSGI app as `app` for gunicorn's default pattern: `gunicorn app:app`
app = get_wsgi_application() 