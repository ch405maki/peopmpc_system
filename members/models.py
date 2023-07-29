from django.db import models
from django.utils.translation import gettext as _
import datetime

def current_datetime():
    return datetime.datetime.now()

class Member(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    CIVIL_STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )

    EDUCATIONAL_ATTAINMENT_CHOICES = (
        ('Elementary', 'Elementary'),
        ('Highschool', 'Highschool'),
        ('Vocational', 'Vocational'),
        ('College', 'College'),
        ('Masters/Doctorate', 'Masters/Doctorate'),
        ('None', 'None'),
    )

    TYPE_OF_ID_CHOICES = (
        ('TIN/BIR', 'TIN / BIR'),
        ('SSS/UMID', 'SSS/UMID'),
        ('PHIC', 'PHIC'),
        ('Voter_ID', "Voter's ID"),
        ('LTO DL', 'LTO DL'),
        ('Student', 'Student'),
        ('Postal', 'Postal'),
        ('Office_ID', 'Office ID'),
        ('Others', 'Others'),
    )

    # Data fields
    name = models.CharField(max_length=100)
    mname = models.CharField(max_length=100, default='')
    lname = models.CharField(max_length=100, default='')
    sname = models.CharField(max_length=100, default='', blank=True)
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    civil_status = models.CharField(max_length=10, null=True, choices=CIVIL_STATUS_CHOICES)
    bplace = models.CharField(max_length=255, null=True, blank=True)
    educational_attainment = models.CharField(max_length=20, choices=EDUCATIONAL_ATTAINMENT_CHOICES, default='None')

    type_of_id1 = models.CharField(max_length=20, null=True, choices=TYPE_OF_ID_CHOICES)
    type_of_id2 = models.CharField(max_length=20, null=True, choices=TYPE_OF_ID_CHOICES)
    type_of_id3 = models.CharField(max_length=20, null=True, choices=TYPE_OF_ID_CHOICES)
    id1_number = models.CharField(max_length=100, default='0')
    id2_number = models.CharField(max_length=100, default='0')
    id3_number = models.CharField(max_length=100, default='0')

    email = models.EmailField()
    profile_picture = models.ImageField(default='profile.png', upload_to='profile_pics')

    def __str__(self):
        return self.name
