# Generated by Django 5.0.8 on 2024-08-12 17:01
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_tag_post_tags'),
    ]

    operations = [
        TrigramExtension()
    ]
