from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    '''
    Custom user class for user registerations. Add all the desired properties here.
    '''
    class Meta:
        unique_together = ('email',)
        verbose_name = 'User'