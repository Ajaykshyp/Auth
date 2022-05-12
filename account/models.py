from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from account.manager import UserManager
# Create your models here.
#custom user authentication

class User(AbstractUser):
    username=None
    email = models.EmailField(unique=True)
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=4,null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
   

   
   