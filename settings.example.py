# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *
import os
DEVELOPMENT_SERVER = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

ROOT_URLCONF = 'urls'

TIME_ZONE='America/Los_Angeles'

ADMINS = (
     ('<username>', '<admin_email@domain.tld>'),
)

ORGANIZATION = 'Organization Name'

MANAGERS = ADMINS

SECRET_KEY = '=r-$b*8hglm+858*9t043hlm6-&6-9d3vfc4((7yd0dbrakhvi'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '%s/media/' % os.path.dirname(os.path.realpath(__file__))

# for django 1.4
STATIC_ROOT = MEDIA_ROOT

## Set SITE_URL to the url of the app engine instance.  For extra security use HTTPS
SITE_URL = "https://nodeshot-gae.appspot.com/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = '%smedia/' % SITE_URL
MEDIA_URL = '/media/'

# for django 1.4
STATIC_URL = MEDIA_URL

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '%sadmin/' % MEDIA_URL
#ADMIN_MEDIA_PREFIX = '/media/admin/'

# From nodeshot settings, and should be tried without being added
TEMPLATE_LOADERS = (
   'django.template.loaders.filesystem.Loader',
   'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# additional information about administrators
AUTH_PROFILE_MODULE = 'nodeshot.UserProfile'

INSTALLED_APPS = (
   'django.contrib.admin',
   'django.contrib.contenttypes',
   'django.contrib.auth',
   'django.contrib.sessions',
   'django.contrib.messages',
   'djangotoolbox',
   'permission_backend_nonrel',
   'nodeshot',
   # djangoappengine should come last, so it can override a few manage.py commands
   'djangoappengine',
)

AUTHENTICATION_BACKENDS = (
   'permission_backend_nonrel.backends.NonrelPermissionBackend',
)

MIDDLEWARE_CLASSES = (
   'django.middleware.common.CommonMiddleware',
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.csrf.CsrfViewMiddleware',
   'django.contrib.auth.middleware.AuthenticationMiddleware',
   'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
#    'django.core.context_processors.request',
   'django.core.context_processors.media',
   'django.contrib.messages.context_processors.messages',
   # nodeshot
   'nodeshot.context_processors.site',
)

SERIALIZATION_MODULES = {
   'json': 'wadofstuff.django.serializers.json'
}

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

TEMPLATE_DIRS = (
   '%s/nodeshot/templates/' % os.path.dirname(os.path.realpath(__file__)),
   os.path.join(os.path.dirname(__file__), 'templates'),
   os.path.join(os.path.dirname(__file__), 'django/contrib/admin/templates'),
)
DBINDEXER_BACKENDS = (
   'dbindexer.backends.BaseResolver',
   'dbindexer.backends.FKNullFix',
   'dbindexer.backends.InMemoryJOINResolver',
)

####### Nodeshot Configuration ###########
#

# google map center for nodeshot
NODESHOT_GMAP_CENTER = {
    'lat': '47.6063889',
    'lng': '-122.3308333'
}

# site name and domain, this is needed for email notifications We wanted to avoid using Django's sites framework
NODESHOT_SITE = {
    'name': 'seattlemesh.net',
    'domain': 'seattlemeshnet-nodeshot.appspot.com'
}

# this setting is used in the generation of KML file
NODESHOT_KML = {
    'name': NODESHOT_SITE['name'],
    'description': 'KML feed for seattlemesh.net generated by Nodeshot.'
}

# routing protocols used in nodeshot.models
NODESHOT_ROUTING_PROTOCOLS = (
    ('aodv','AODV'),
    ('batman','B.A.T.M.A.N.'),
    ('dsdv','DSDV'),
    ('dsr','DSR'),
    ('hsls','HSLS'),
    ('iwmp','IWMP'),
    ('olsr','OLSR'),
    ('oorp','OORP'),
    ('ospf','OSPF'),
    ('tora','TORA'),
)

# set your default routing protocol
NODESHOT_DEFAULT_ROUTING_PROTOCOL = 'olsr'
# maximum number of days to activate a new node until is purged (automatic purging needs a cronjob to be set on the server)
NODESHOT_ACTIVATION_DAYS = 7
# log messages sent with contact form
NODESHOT_LOG_CONTACTS = True

_ = lambda s: s

NODESHOT_FRONTEND_SETTINGS = {
    'META_ROBOTS': 'noindex,nofollow',
    'SHOW_STATISTICS': True,
    'SHOW_KML_LINK': True,
    'HELP_URL': 'http://wiki.ninux.org/UsareMapserver',
    'SHOW_ADMIN_LINK': True,
    'TAB3': 'OLSR',
    'TAB4': 'VPN',
    'WELCOME_TEXT': _('Welcome to Nodeshot!'),
    'LINK_QUALITY': 'etx' # dbm, etx
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
# Ensure that the domain is in the form of app-name.appspotmail.com or notifications will fail to be sent
DEFAULT_FROM_EMAIL = 'noreply@seattlemeshnet-nodeshot.appspotmail.com'

# captcha settings
MATH_CAPTCHA_NUMBERS = range(1,999)
MATH_CAPTCHA_OPERATORS = '+'
MATH_CAPTCHA_QUESTION = _('Antispam question: what is the sum of')



#
####### End Nodeshot Configuration #######

# Activate django-dbindexer if available
try:
    import dbindexer
    DATABASES['native'] = DATABASES['default']
    DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
    INSTALLED_APPS += ('dbindexer',)
    DBINDEXER_SITECONF = 'dbindexes'
    MIDDLEWARE_CLASSES = ('dbindexer.middleware.DBIndexerMiddleware',) + \
                         MIDDLEWARE_CLASSES
except ImportError:
   pass
