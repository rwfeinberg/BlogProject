from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Defines signal to create profile on user creation
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Defines signal to update and save profile correctly
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()