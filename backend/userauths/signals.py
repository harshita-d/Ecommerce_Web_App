from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that runs *after* a User is saved.
    - `sender` is the model class (User).
    - `instance` is the actual User object just saved.
    - `created` is a boolean: True if this was a brand-new object.
    - `**kwargs` can include other args (e.g., update_fields).
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver that also runs after a User is saved.
    Ensures the linked Profile is saved whenever the User is saved.
    """
    instance.profile.save()
