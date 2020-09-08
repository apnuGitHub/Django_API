from django.db import models
from django import forms

from django.db import models

class Hero(models.Model):
    title   = models.CharField(max_length=20, null=False, blank=False)
    para    = models.TextField(max_length=5000, null=False, blank=False)
    #file = forms.FileField()
    #alias = models.CharField(max_length=60)
    def __str__(self):
        return self.title

# Create your models here.
