from django.contrib.auth.backends import ModelBackend # default backend
from django.contrib.auth.models import User, Permission

# Overwrite the default backend to check for e-mail address 
class EmailModelBackend(ModelBackend):

    def authenticate(self, username = None, password = None):
        #If username is an email address, then try to pull it up
        if '@' in username:
            try:
                user = User.objects.get(email = username)
            except User.DoesNotExist:
                return None

        else:
            #We have a non-email address username we should try username
            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                return None

        if user.check_password(password):
            return user
