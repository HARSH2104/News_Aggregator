
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TeamBitsAndBytes_NewsAggregator.settings')

application = get_wsgi_application()
