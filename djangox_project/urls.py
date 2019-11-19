from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from users.views import MySignupView
from allauth.account.views import LoginView, EmailView
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', MySignupView.as_view(), name="home"),
    #path('accounts/', include('allauth.urls')),
    #path('users/', include('django.contrib.auth.urls')),
    #path('accounts/confirm-email/<slug>/',  ConfirmEmailView.as_view(), name='account_confirm_email'),
]
urlpatterns += i18n_patterns(
    path('', include('pages.urls')),
    path('', MySignupView.as_view(), name='account_signup_custom'), 
    path('', MySignupView.as_view(), name='home'), 
    path(_('accounts/'), include('allauth.urls')),
    path(_('accounts/login'), MySignupView.as_view(), name='account_login'), 
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns+= [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

