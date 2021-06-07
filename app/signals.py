from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile
from django.contrib.auth.signals import user_logged_in, user_logged_out


@receiver(post_save, sender=User)
def user_created_profile(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('Profile created!')


@receiver(post_save, sender=User)
def user_updated_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(user_logged_in, sender=User)
def user_login(user, request, *args, **kwargs):
    print('User {} success login from '.format(
        user.username), request.META.get('HTTP_REFERER'))


@receiver(user_logged_out)
def user_logout(request, user, *args, **kwargs):
    print('User {} logout from'.format(user.username),
          request.META.get('HTTP_REFERER'))
