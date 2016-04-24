from __future__ import unicode_literals
from datetime import datetime


from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100000)
    create_time = models.DateField(default=datetime.now(), blank=True)
    update_time = models.DateField(default=datetime.now(), blank=True)
    author = models.CharField(max_length=200)

