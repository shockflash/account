from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import never_cache
from django.contrib.sites.models import Site, RequestSite
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

@never_cache
def login(request, template_name = 'registration/login.html',
          redirect_field_name = REDIRECT_FIELD_NAME,
          authentication_form = AuthenticationForm):
    """
    Displays the login form and handles the login action.
    I use an own version to disable csrf checks here. The login form is often
    called from different locations, like a frontpage, which could be heavily
    cached. To prevent such problems, we offer a csrf-disabled version here.
    """

    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data = request.POST)
        if form.is_valid():
            # Light security check -- make sure redirect_to isn't garbage. 
            if not redirect_to or ' ' in redirect_to:
                redirect_to = settings.LOGIN_REDIRECT_URL

            # Heavier security check -- redirects to http://example.com should. 
            # not be allowed, but things like /view/?param=http://example.com. 
            # should be allowed. This regex checks if there is a '//' *before* a 
            # question mark. 
            elif '//' in redirect_to and re.match(r'[^\?]*//', redirect_to):
                    redirect_to = settings.LOGIN_REDIRECT_URL

            # Okay, security checks complete. Log the user in. 
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)

    else:
        form = authentication_form(request)

    request.session.set_test_cookie()

    if Site._meta.installed:
        current_site = Site.objects.get_current()
    else:
        current_site = RequestSite(request)

    return render_to_response(template_name, {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }, context_instance = RequestContext(request))
