from django.urls import path

from .views import HomePageView, AboutPageView, ThankYouView, AccountHomeView

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('thankyou/', ThankYouView.as_view(), name='thankyou'),
    path('account-home/', AccountHomeView.as_view(), name='account_home'),
]
