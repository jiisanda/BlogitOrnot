from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User,null = True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, default='default_profile.jpg')
    portfolio_site = models.URLField(blank=True)
    github_username = models.CharField(max_length=20, blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    twitter_username = models.CharField(max_length=20, blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_username = models.CharField(max_length=20, blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    facebook_username = models.CharField(max_length=20, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return str(self.user.username)

def create_profile(sender, instance, created, *args, **kwargs):
    # ignore if this is an existing User
    if not created:
        return
    Profile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)