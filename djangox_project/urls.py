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
    path('', MySignupView.as_view(), name="home"),
    #path('admin/', admin.site.urls),
    #path('accounts/', include('allauth.urls')),
    #path('users/', include('django.contrib.auth.urls')),
]
urlpatterns += i18n_patterns(
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('userprofile/api/v1/', include('userprofile.urls')),
    path('', MySignupView.as_view(), name='home'), 
    path('', MySignupView.as_view(), name='account_signup_custom'), 
    path(_('accounts/'), include('allauth.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns+= [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

