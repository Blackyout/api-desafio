import os
from django.core.wsgi import get_wsgi_application

# Por defecto usa dev si no está seteado
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')

application = get_wsgi_application()