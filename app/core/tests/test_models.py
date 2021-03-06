from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@gmail.com"
        password = "password"
        user = get.user.model().objects.create_user(
            email=email,
            password=password
        )

        self.assertQual(user.email, email)
        self.assertTrue(user,check_password(password))
