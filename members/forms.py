from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'mname', 'lname', 'sname', 'birthday', 'age', 'bplace', 'email', 'profile_picture', ]
