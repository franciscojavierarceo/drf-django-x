from rest_framework import generics, permissions
from .permissions import IsUserOrReadOnly
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsUserOrReadOnly,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer