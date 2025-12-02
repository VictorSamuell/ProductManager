from django.shortcuts import redirect
from django.urls import reverse, NoReverseMatch
from django.conf import settings


class LoginRequiredMiddleware:
    """
    Redirect anonymous users to the login page for all views except a small whitelist.
    Configure additional exempt URLs in `settings.LOGIN_EXEMPT_URLS` if needed.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info
        exempt_urls = getattr(settings, 'LOGIN_EXEMPT_URLS', [])
        # Add default auth-related endpoints
        try:
            exempt_urls.extend([
                reverse('login'),
                reverse('logout'),
                reverse('registro'),
            ])
        except NoReverseMatch:
            # reverse() may fail during startup; ignore and continue
            pass

        # Always allow admin and static/media
        exempt_url_prefixes = ['/admin/', settings.STATIC_URL, getattr(settings, 'MEDIA_URL', '/media/')]

        if not request.user.is_authenticated:
            if any(path.startswith(prefix) for prefix in exempt_url_prefixes):
                return self.get_response(request)
            if path in exempt_urls:
                return self.get_response(request)
            # Redirect to login with next parameter
            try:
                login_url = reverse('login')
            except NoReverseMatch:
                login_url = settings.LOGIN_URL
            return redirect(f"{login_url}?next={request.path}")

        return self.get_response(request)
