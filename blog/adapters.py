from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Custom adapter for django-allauth to override default behaviors
    """
    def get_login_redirect_url(self, request):
        """
        Override to customize redirect URL after login
        """
        path = "/"
        return path

    def get_signup_redirect_url(self, request):
        """
        Override to customize redirect URL after signup
        """
        path = "/"
        return path
