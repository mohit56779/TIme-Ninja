# Generated by Django 3.2.5 on 2021-07-21 07:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Userprofile',
            new_name='Project',
        ),
    ]
