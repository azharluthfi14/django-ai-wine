from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(
        default='default.jpg',
        upload_to='user_profile_picture',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        width, height = img.size

        if width > 300 and height > 300:
            img.thumbnail((width, height))

        if height < width:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
        elif width < height:
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))
        if width > 300 and height > 300:
            img.thumbnail((300, 300))
        img.save(self.image.path)


class WineClassification(models.Model):

    fixed_acidity = models.FloatField()
    volatile_acidity = models.FloatField()
    citric_acid = models.FloatField()
    residual_sugar = models.FloatField()
    chlorides = models.FloatField()
    free_sulfur_dioxide = models.FloatField()
    total_sulfur_dioxide = models.FloatField()
    density = models.FloatField()
    pH = models.FloatField()
    sulphates = models.FloatField()
    alcohol = models.FloatField()
    classification = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.classification
