from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary.uploader

class Project(models.Model):
    """
    Model representing a project.
    Each project has an ID (automatically generated), a title, a description, and image resources.
    """
    TYPE_CHOICES = [
        ('design', 'Design'),
        ('illustration', 'Illustration'),
    ]

    title_en = models.CharField(max_length=255, blank=True, null=True)
    title_es = models.CharField(max_length=255, blank=True, null=True)
    title_ca = models.CharField(max_length=255, blank=True, null=True)

    description_en = models.TextField(blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    description_ca = models.TextField(blank=True, null=True)

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title_en

class ProjectImage(models.Model):
    """
    Model to storage the multiple images related to a project.
    """
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image_resources')

    def __str__(self):
        return f"Imagen para {self.project.title_en}"

    def delete(self, *args, **kwargs):
        """
        Ensure that a Cloudinary image is removed when it's removed from the model instance.
        """
        if self.image:
            cloudinary.uploader.destroy(self.image.public_id)
        super().delete(*args, **kwargs)
