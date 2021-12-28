from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    note_content = models.TextField(blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ('title',)
    
    def __str__(self):
        return self.title
    