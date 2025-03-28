# Generated by Django 5.1.7 on 2025-03-16 09:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_resources',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='image_resources'),
            preserve_default=False,
        ),
    ]
