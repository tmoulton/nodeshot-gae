from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import connection, transaction
from django.conf import settings
import random
import string
from datetime import datetime
class AddressableObject(models.Model):
    address_1 = models.CharField(max_length=50, blank=True, null=True)
    address_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    class Meta:
        abstract = True
        
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    current_household = models.ForeignKey(Household)
    paypal_address = models.EmailField()
    
    def __unicode__(self):
        return self.user.__unicode__()
        
class HouseholdUser(models.Model):
    user = models.ForeignKey(User, unique=True)
    household = models.ForeignKey(Household)
    move_in_date = models.DateField()
    move_out_date = models.DateField()
    active = models.BooleanField(default=True)
    
class Household(AddressableObject):
    name = models.char(max_length=255,null=False)
    
    def get_current_users(self):
        return UserProfile.objects.filter(current_household=self)
    def get_active_definitions(self):
        return Definition.objects.filter(household=self,active=True)
        
