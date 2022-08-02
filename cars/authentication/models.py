from enum import unique
from turtle import mode
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# * imported for email validation
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager): 
    # * Overwriting the [create_user, create_superuser] methods
    # * [create_user] will allow us to create our user object
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should be provided"))
            # * [normalize_email] will change the letters in the email to lowercase.
        email     = self.normalize_email(email)
        new_user  = self.model(email = email, **extra_fields)
        # * [set_password] will get the password for the new user it hashes it and store it inside the database.
        new_user.set_password(password)
        new_user.save()
        return new_user
            

    # * Takes care of the requires fields as well as the extra fields 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as True"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active as True"))
        
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    Email    = models.EmailField(max_length = 120, unique = True)
        