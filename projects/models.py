from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
