from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number1 = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    phone_number2 = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    portfolio_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    def __str__(self):
        return self.user.username

