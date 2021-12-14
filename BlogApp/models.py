from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    writer = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    def __str__(self) -> str:
        return self.user.username

