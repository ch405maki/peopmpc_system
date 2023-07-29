from django import forms
from .models import Member

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
            'bplace',
            'email',
            'gender',
            'civil_status',
            'educational_attainment',
            'type_of_id1',
            'type_of_id2',
            'type_of_id3',
            'id1_number',
            'id2_number',
            'id3_number',
            'profile_picture',
        ]