DEBUG = True
ALLOWED_HOSTS = ['localhost', 'smbackend.kontena.hel.ninja']

grr='''DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'smbackend',
        'CONN_MAX_AGE': 600,
    }
}'''

STATIC_ROOT = BASE_DIR + '/home/smbackend/static'
STATIC_URL = BASE_DIR + '/servicemap/static/'

