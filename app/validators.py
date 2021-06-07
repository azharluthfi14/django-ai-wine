from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_email_unique(email):
    email_check = User.objects.filter(email=email)
    if email_check:
        raise ValidationError(f"Email address %s already registered." % email)


def validate_username_unique(username):
    username_check = User.objects.filter(username=username)
    if username_check:
        raise ValidationError(f"Username %s already taken." % username)
