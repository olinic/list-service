import os
from dotenv import load_dotenv
load_dotenv()

DJANGO_SECRET = os.environ.get('DJANGO_SECRET', 'django-insecure-2v(tyxph8xg(q#giyg2#-&$b@blsf$y0_gpl!=5!)6-#zsb4fc')
DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG', False)
TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')
