from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_investor = models.BooleanField(default= False)
  is_inventor = models.BooleanField(default = False)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email_address = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  country = models.CharField(max_length=200)

  def __str__(self) :
      return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
      if created:
            Token.objects.create(user=instance)


class investor(models.Model):
    user = models.OneToOneField(
     User, on_delete=models.CASCADE, blank=True, null=True, related_name="investor")
    is_investor = models.BooleanField(default= True, null=True)
    company_name = models.CharField(max_length=200, null=True)
    company_email = models.CharField(max_length=200, null=True)
    company_address = models.CharField(max_length=200, null=True)
    head_office = models.CharField(max_length=200, null=True)
    hobbies = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    facabook_url = models.CharField(max_length=200, null=True)
    linkedin_url = models.CharField(max_length=200, null=True)
    
    # def __str__(self) :
    #     #   return self.username 
    #     pass


     


class inventor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    is_inventor = models.BooleanField(default = True, null=True)
    company_name = models.CharField(max_length=200, null=True)
    company_email = models.CharField(max_length=200, null=True)
    company_address = models.CharField(max_length=200, null=True)
    head_office = models.CharField(max_length=200, null=True)
    hobbies = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    facabook_url = models.CharField(max_length=200, null=True)
    linkedin_url = models.CharField(max_length=200, null=True)

    # def __str__(self) :
    #     #   return self.username 
    #     pass









