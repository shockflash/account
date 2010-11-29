from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationFormUniqueEmail


# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = {'class': 'required'}


class RegistrationFormUniqueEmailUsername(RegistrationFormUniqueEmail):

    class Meta:
        fields = ('example')

    username = False
    example = forms.CharField(label = "Example")
