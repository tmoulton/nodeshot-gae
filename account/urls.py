from django.conf.urls.defaults import *



handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^$', 'views.index'),
    (r'register$', 'views.register'),
    (r'reset_password$','django.contrib.auth.views.password_reset'),
    (r'reset_password_done$','django.contrib.auth.views.password_reset_done'),
    (r'reset_password_confirm/(?P<uidb64>.+)/(?P<token>.+)$','django.contrib.auth.views.password_reset_confirm'),
    (r'reset_password_complete$','django.contrib.auth.views.password_reset_complete'),

   # (r'register$', 'views.register'),
#    (r'^use/(?P<code>.+)/$', 'tickets.txqueue.views.use_code'),
#    ('^$', 'django.views.generic.simple.direct_to_template',
#     {'template': 'home.html'}),
)
