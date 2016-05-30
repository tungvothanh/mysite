from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# noi chung la cai nay khong can form van okie
# van de la custom no nhg the nao ma thoi.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    def __unicode__(self):
        return self.user.username