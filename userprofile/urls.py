from django.urls import path

from .views import UserProfileList, UserProfileDetail

urlpatterns = [
    path('<int:pk>/', UserProfileDetail.as_view()),
    path('', UserProfileList.as_view()),
]