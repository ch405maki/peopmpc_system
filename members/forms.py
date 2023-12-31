from django import forms
from .models import Member
import random

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'name',
            'mname',
            'lname',
            'sname',
            'birthday',
            'age',
            'gender',
            'civil_status',
            'bplace',
            'educational_attainment',
            'type_of_id1',
            'type_of_id2',
            'type_of_id3',
            'id1_number',
            'id2_number',
            'id3_number',
            'permanent_street',
            'permanent_purok',
            'permanent_barangay',
            'permanent_city',
            'permanent_province',
            'current_street',
            'current_purok',
            'current_barangay',
            'current_city',
            'current_province',
            'years_residence',
            'contact_number',
            'email',
            'occupation',
            'employer_name',
            'nature_of_work',
            'years_in_service',
            'employer_contact_number',
            'annual_income',
            'employer_street',
            'employer_purok',
            'employer_barangay',
            'employer_city',
            'employer_province',
            'slname',
            'sfname',
            'smname',
            'ssname',
            'sbirthday',
            'sage',
            'sbplace',
            'seducational_attainment',
            'profile_picture',
            'account_number',
            'status',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account_number'].required = False

        # Generate a random account number and set it as the initial value
        random_account_number = random.randint(100000, 999999)
        self.fields['account_number'].initial = random_account_number