"""
Model definition for our user profiles
users will have first name last name
and email
"""
from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    """
    User Model
    """
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

