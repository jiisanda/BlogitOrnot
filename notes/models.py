from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=30)
    note_content = models.TextField(blank=True, null=True)

    class Meta():
        ordering = ('title',)