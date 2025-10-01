import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_dynamic_form_tutorial1.settings')
application = get_wsgi_application()
