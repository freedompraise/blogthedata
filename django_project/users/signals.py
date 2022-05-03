from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# from admin_honeypot.signals import honeypot
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(instance, **kwargs):
    instance.profile.save()

# @receiver(honeypot)
# def my_callback(sender, **kwargs):
#     print("Request finished!")
    