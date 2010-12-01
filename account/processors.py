from django.contrib.auth.forms import AuthenticationForm

def login(request):
    return {
        # make Loginform available on all pages
        'loginform': AuthenticationForm(),
    }


def login(request):

    fb = None
    try:
        fb = request.facebook2
    except:
        pass

    return {
        # make facebook user object available on all pages
        'facebook': fb,
    }
