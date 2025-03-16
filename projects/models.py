from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    """
    Model representing a project.
    Each project has an ID (automatically generated), a title, a description, and image resources.
    """
    TYPE_CHOICES = [
        ('design', 'Design'),
        ('illustration', 'Illustration'),
    ]

    title_en = models.CharField(max_length=255)
    title_es = models.CharField(max_length=255, blank=True, null=True)
    title_ca = models.CharField(max_length=255, blank=True, null=True)

    description_en = models.TextField()
    description_es = models.TextField(blank=True, null=True)
    description_ca = models.TextField(blank=True, null=True)

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title_en

class ProjectImage(models.Model):
    """
    Model for storing multiple images related to a project.
    """
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image_resources')

    def __str__(self):
        return f"Image for {self.project.title_en}"
