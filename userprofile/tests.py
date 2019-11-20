from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import UserProfile 

class UserProfileTests(TestCase):
    @classmethod

    # Creating a user and profile
    def setUpTestData(cls):
        User = get_user_model()
        #User = settings.AUTH_USER_MODEL
        testuser1 = User.objects.create_user(
            email='test@test.com',
            username='test_test_com',
            password='abc123'
        )
        testuser1.save()

        test_user_profile1 = UserProfile.objects.create(
            user=testuser1, 
            title='Dr',
            first_name='Tom',
            middle_name='Test',
            last_name='Test',
            gross_annual_income=100000
        ) 
        test_user_profile1.save()

    def test_user_profile_content(self):
        userprofile = UserProfile.objects.get(id=1)
        expected_user = f'{userprofile.user}'
        expected_title = f'{userprofile.title}'
        expected_first_name = f'{userprofile.first_name}'
        expected_middle_name = f'{userprofile.middle_name}'
        expected_last_name = f'{userprofile.last_name}'
        expected_income = 100000
        self.assertEqual(expected_first_name, 'Tom')
        self.assertEqual(expected_middle_name, 'Test')
        self.assertEqual(expected_last_name, 'Test')
        self.assertEqual(expected_title, 'Dr')
        self.assertEqual(expected_income, 100000)