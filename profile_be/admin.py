from django.contrib import admin
from .models import *


# Register your models here.

class ContactViewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


admin.site.register(ContactView, ContactViewAdmin)
