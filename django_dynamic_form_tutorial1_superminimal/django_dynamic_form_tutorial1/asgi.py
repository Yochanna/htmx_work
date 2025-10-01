import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_dynamic_form_tutorial1.settings')
application = get_asgi_application()
