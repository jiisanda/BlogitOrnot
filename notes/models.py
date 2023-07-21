from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=30, blank=False, null=False, default="Title")
    note_content = models.TextField(blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ('title',)
    
    def __str__(self):
        return '%s - %s' % (self.title, self.user)
    