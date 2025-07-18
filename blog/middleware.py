from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve, Resolver404

EXEMPT_URLS = ['login', 'logout', 'admin:login']

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info

        try:
            current_url = resolve(path).url_name
        except Resolver404:
            current_url = None

        # Skip for authenticated users
        if request.user.is_authenticated:
            return self.get_response(request)

        # Allow exempt URLs and media/static paths
        if (
            current_url in EXEMPT_URLS or
            path.startswith(settings.STATIC_URL) or
            path.startswith(settings.MEDIA_URL)
        ):
            return self.get_response(request)

        # Default redirect to login
        print(f"[Middleware] Blocking unauthenticated access to: {request.path}")
        return redirect(settings.LOGIN_URL)
