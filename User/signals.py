from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

from .models import User

@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):

    if created:

        # if instance.is_staff:
        #     staff_group, _ = Group.objects.get_or_create(name='Staff')
        #     instance.groups.add(staff_group)
        
        # elif instance.is_superuser:
        #     superuser_group, _ = Group.objects.get_or_create(name='Super Users')
        #     instance.groups.add(superuser_group)

        # else:
        #     regularuser_group, _ = Group.objects.get_or_create(name='Regular User')
        #     instance.groups.add(regularuser_group)

            pass