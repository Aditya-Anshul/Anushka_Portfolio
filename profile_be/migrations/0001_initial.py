# Generated by Django 3.2.3 on 2022-10-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
    ]