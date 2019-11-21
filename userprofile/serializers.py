from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'user', 'title', 'first_name', 'middle_name', 'last_name', 'gross_annual_income', 'created_at', 'updated_at',)
        model = UserProfile

