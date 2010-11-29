from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import socialregistration.urls
import forms

urlpatterns = patterns('',

    (r'^register/', 'registration.views.register',
            {'form_class': forms.RegistrationFormUniqueEmailUsername,
             'backend': 'registration.backends.default.DefaultBackend'}),

    url(r'^fslogin/', 'account.views.login', name = 'auth_fslogin'),
    (r'^profiles/', include('profiles.urls')),
    (r'^social/', include(socialregistration.urls)),
    (r'^', include('registration.urls')),
)
