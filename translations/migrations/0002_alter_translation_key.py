# Generated by Django 5.1.7 on 2025-04-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='key',
            field=models.CharField(help_text='Key example: WRITE_IT_LIKE_THIS_EXAMPLE', max_length=255),
        ),
    ]
