from django.db import models


# Create your models here.

class ContactView(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=50, default='')
    message = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name
