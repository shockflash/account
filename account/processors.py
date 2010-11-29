from django.contrib.auth.forms import AuthenticationForm

def login(request):
    return {
        'loginform': AuthenticationForm(),
    }
