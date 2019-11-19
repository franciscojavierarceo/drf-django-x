from django.urls import path
from .views import SignUpPageView
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', SignUpPageView.as_view(), name='account_signup_custom'), 
    path('', SignUpPageView.as_view(), name='home'), 
    path(_('accounts/login'), SignUpPageView.as_view(), name='account_login'), 
]