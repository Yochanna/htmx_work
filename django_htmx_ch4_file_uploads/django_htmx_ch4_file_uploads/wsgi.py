import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_htmx_ch4_file_uploads.settings')
application = get_wsgi_application()
