from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    """
    creates a Profile each time a new User is created
    """
    # print(f"sender: {sender}\ninstance: {instance}") #
    # sender: <class 'django.contrib.auth.models.User'>
    # instance: test2

    if created:
        Profile.objects.create(user=instance)
