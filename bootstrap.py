from django.contrib.auth.models import User
import logging
if User.objects.count() == 0:
    user = User.objects.create_user('<username>', '<password>', '<password>')
    
    # At this point, user is a User object that has already been saved
    # to the database. You can continue to change its attributes
    # if you want to change other fields.
    user.is_staff = True
    user.is_superuser = True
    user.save()
    logging.debug("Super user created")
else:
    logging.debug("Bootstrap called with existing users!")
    

