# create the user profile

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    address = models.TextField(default='', null=True, blank=True)
    phone = models.TextField(max_length=255,default='', null=True, blank=True)


    # Signal to create Profile when a User is created
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)