from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Relationship


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


@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    """
    gets the sender and receiver; checks if the status is accepted,
    and add the receiver to the senders' friends list and the sender to the receivers friends list
    """
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        receiver_.save()
        sender_.save()
    if created:
        Profile.objects.create(user=instance)
