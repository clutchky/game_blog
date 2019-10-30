from django.db.models.signals import post_save # signal that gets fired after an object is saved
from django.contrib.auth.models import User # sends the post_save signal when a new user is created
from django.dispatch import receiver # a function that gets the signal and performs a task
from .models import Profile # the object that is created

@receiver(post_save, sender=User) # docs.djangoproject.com/en/2.2/ref/signals/#post-save
def create_profile(sender, instance, created, **kwargs): 
    if created: # if a user was created
        Profile.objects.create(user=instance) # create a Profile object with the user=instance

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save() # user=instance