from __future__ import unicode_literals

from django.db import models
# from django import forms
# tan 8h moi dcv ma nday gio kblgi


# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
