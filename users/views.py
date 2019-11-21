from allauth.account.views import SignupView
from django.utils.translation import gettext_lazy as _
from users.forms import CustomUserCreationForm
from django.utils import translation

class MySignupView(SignupView):
    form_class = CustomUserCreationForm
    context = {
        'available_languages': ['en', 'es'],
    }
    def get(self, request, *args, **kwargs):
        """
        This is the main page where we set the default language 
        and allow for the URL to identify the user's preferred language
        """
        user_language = None

        try:
            user_language = request.path.split("/")[1]
        except:
            pass

        if user_language:
            pass
        else:
            if translation.LANGUAGE_SESSION_KEY in request.session:
                user_language = request.session[translation.LANGUAGE_SESSION_KEY]
            else:
                user_language = 'es'
        translation.activate(user_language)
        request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        return super().get(self, request, *args, **kwargs)