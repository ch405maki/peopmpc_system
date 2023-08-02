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

    OCCUPATION_CHOICES = (
        ('Farming/Agriculture', 'FARMING / AGRICULTURE'),
        ('Private Employee', 'PRIVATE EMPLOYEE'),
        ('Government Employee', 'GOVERNMENT EMPLOYEE'),
        ('Self Employed/Business', 'SELF EMPLOYED / BUSINESS'),
        ('Student', 'STUDENT'),
        ('Overseas Filipino Worker', 'OVERSEAS FILIPINO WORKER'),
    )

    ANNUAL_INCOME_CHOICES = (
        ('P10,000.00–P50,000.00', 'P10,000.00–P50,000.00'),
        ('P51,000.00–P100,000.00', 'P51,000.00–P100,000.00'),
        ('P101,000.00–P150,000.00', 'P101,000.00–P150,000.00'),
        ('P150,000.00 Above', 'P150,000.00 Above'),
    )

    STATUS_CHOICES = (
        ('approve', 'Approve'),
        ('pending', 'Pending'),
        ('disapprove', 'Disapprove'),
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

    permanent_street = models.CharField(max_length=100, null=True)
    permanent_purok = models.CharField(max_length=100, null=True)
    permanent_barangay = models.CharField(max_length=100, null=True)
    permanent_city = models.CharField(max_length=100, null=True)
    permanent_province = models.CharField(max_length=100, null=True)

    current_street = models.CharField(max_length=100, null=True)
    current_purok = models.CharField(max_length=100, null=True)
    current_barangay = models.CharField(max_length=100, null=True)
    current_city = models.CharField(max_length=100, null=True)
    current_province = models.CharField(max_length=100, null=True)

    years_residence = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=100, null=True)
    email = models.EmailField()

    occupation = models.CharField(max_length=50, null=True, choices=OCCUPATION_CHOICES)
    employer_name = models.CharField(max_length=100, null=True)
    nature_of_work = models.CharField(max_length=100, null=True)
    years_in_service = models.PositiveIntegerField(null=True)
    employer_contact_number = models.CharField(max_length=20, null=True)
    annual_income = models.CharField(max_length=50, null=True, choices=ANNUAL_INCOME_CHOICES)

    employer_street = models.CharField(max_length=100, null=True)
    employer_purok = models.CharField(max_length=100, null=True)
    employer_barangay = models.CharField(max_length=100, null=True)
    employer_city = models.CharField(max_length=100, null=True)
    employer_province = models.CharField(max_length=100, null=True)

    sfname = models.CharField(max_length=100, null=True)
    smname = models.CharField(max_length=100, default='')
    slname = models.CharField(max_length=100, default='')
    ssname = models.CharField(max_length=100, default='')
    sbirthday = models.DateField(null=True, blank=True)
    sage = models.IntegerField(null=True)
    sbplace = models.CharField(max_length=255, null=True, blank=True)
    seducational_attainment = models.CharField(max_length=20, choices=EDUCATIONAL_ATTAINMENT_CHOICES, default='None')

    account_number = models.IntegerField(null=True, unique=True)
    status = models.CharField(max_length=20, default='pending', choices=STATUS_CHOICES)

    profile_picture = models.ImageField(default='profile.png', upload_to='profile_pics')

    def __str__(self):
        return self.name
