
import environ

root = environ.Path(__file__) - 2  # two folders back
env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, ''),
    ALLOWED_HOSTS=(list, []),
    DATABASE_URL=(str, 'postgis:///smbackend'),
    MEDIA_ROOT=(environ.Path(), root('media')),
    STATIC_ROOT=(environ.Path(), root('static')),
    MEDIA_URL=(str, '/media/'),
    STATIC_URL=(str, '/static/'),
    COOKIE_PREFIX=(str, 'smbackend'),
    SECURE_PROXY_SSL = (bool, False)
)

environ.Env.read_env()

DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
ADMINS = env('ADMINS')

DATABASES = {
    'default': env.db()
}

STATIC_URL = env('STATIC_URL')
MEDIA_URL = env('MEDIA_URL')
STATIC_ROOT = env('STATIC_ROOT')
MEDIA_ROOT = env('MEDIA_ROOT')

if env('SECURE_PROXY_SSL'):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
