# Generated by Django 3.2.3 on 2022-11-19 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_be', '0002_rename_react_reactview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReactView',
            new_name='ContactView',
        ),
    ]