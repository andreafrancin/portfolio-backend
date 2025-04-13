from django.db import models

# Create your models here.
class Translation(models.Model):
    key = models.CharField(
        max_length=255, 
        blank=False, 
        null=False, 
        help_text="Key example: WRITE_IT_LIKE_THIS_EXAMPLE"
    )
    text_en = models.TextField(blank=False, null=False)
    text_es = models.TextField(blank=False, null=False)
    text_ca = models.TextField(blank=False, null=False)