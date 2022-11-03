from django.core import validators
from django import forms

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('started with a')
def check_for_len(v):
    if len(v)<5:
        raise forms.ValidationError('length issues')

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100,validators=[check_for_a,validators.MaxLengthValidator(5)])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    email=forms.EmailField(max_length=100)
    reenter_email=forms.EmailField(max_length=100)
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])


    def clean_botcatcher(self):
        data=self.cleaned_data['botcatcher']
        if len(data)>0:
            raise forms.ValidationError('bot')
    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reenter_email']
        if e!=r:
            raise forms.ValidationError('emails not matched')
