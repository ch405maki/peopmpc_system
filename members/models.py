from django.db import models
from django.utils.translation import gettext as _
import datetime

def current_datetime():
    return datetime.datetime.now()

class Member(models.Model):

    # Data fields
    name = models.CharField(max_length=100)
    mname = models.CharField(max_length=100, default='')
    lname = models.CharField(max_length=100, default='')
    sname = models.CharField(max_length=100, default='', blank=True)
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    bplace = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    profile_picture = models.ImageField(default='profile.png', upload_to='profile_pics')

    def __str__(self):
        return self.name
