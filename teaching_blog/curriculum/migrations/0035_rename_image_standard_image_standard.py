# Generated by Django 4.0.5 on 2023-01-08 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0034_alter_standard_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standard',
            old_name='image',
            new_name='image_standard',
        ),
    ]
