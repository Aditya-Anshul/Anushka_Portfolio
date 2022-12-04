from rest_framework import serializers
from .models import *
from django import forms
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactView
        fields = ['name', 'email', 'message']

        def save(self, commit=True):
            user = super(self).save(commit=False)
            user.name= self.cleaned_data['name']
            user.email = self.cleaned_data['email']
            user.message = self.cleaned_data['message']
            if commit:
                user.save()
            return user
