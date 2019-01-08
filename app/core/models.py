from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def creat_user(self, email, password, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Customer user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_doner = models.BooleanField(default=False)
    is_donee = models.BooleanField(default=False)
    point_of_contact = models.CharField(max_length=200)
    company_name = models.CharField(max_length=250)
    company_type = models.CharField(max_length=250)
    company_logo_image = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    street_address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField(default=98144)

    objects = UserManager()

    USERNAME_FIELD = 'email'
