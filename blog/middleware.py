from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve, Resolver404

EXEMPT_URLS = [
    'login',
    'logout',
    'admin:login',
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            current_url = resolve(request.path_info).url_name
        except Resolver404:
            current_url = None  # In case the URL can't be resolved

        if not request.user.is_authenticated:
            if current_url not in EXEMPT_URLS:
                return redirect(settings.LOGIN_URL)

        return self.get_response(request)
