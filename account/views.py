from google.appengine.api import users

from django.http import HttpResponse
from django.views.generic.simple import direct_to_template, redirect_to
#from models import *

from datetime import datetime
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail, EmailMessage
from random import Random
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required


def index(request):
    if User.is_authenticated:
        greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
                    (User.get_full_name, '/accounts/logout'))
    else:
        greeting = ("<a href=\"%s\">Sign in</a>." %
                    '/accounts/login')
    
#    user = users.get_current_user()
#    if user:
#        greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
#                    (user.nickname(), users.create_logout_url("/")))
#    else:
#        greeting = ("<a href=\"%s\">Sign in or register</a>." %
#                    users.create_login_url("/"))
#        
    return direct_to_template(request,'home.html',
                              {'login_greeting': greeting, 'user': User})
    
    
@login_required(login_url='/_ah/login',redirect_field_name='continue')
def bills(request):
    user = users.get_current_user()
    if user:
        greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
                    (user.nickname(), users.create_logout_url("/")))
    else:
        greeting = ("<a href=\"%s\">Sign in or register</a>." %
                    users.create_login_url("/"))
        
    return direct_to_template(request,'home.html',
                        {'login_greeting': greeting,
                         'message': 'Bills'})
    