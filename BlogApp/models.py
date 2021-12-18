from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, )

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

class Post(models.Model):
    title=models.CharField(max_length=200)
    writer = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    post_date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=225, default="Just a post...")
    post_picture = models.ImageField(upload_to='post_pictures', blank=True, null=True, 
                                        default='post_pictures/Blog-It-Or-Not.png')

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.writer)
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    def __str__(self) -> str:
        return self.user.username

