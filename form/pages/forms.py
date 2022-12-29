from django import forms
from pages.models import employee
from django.forms import ValidationError
#server side validation
class valid(forms.Form):
    name = forms.CharField(required=False)
    username = forms.CharField(required=True)
    password = forms.CharField(required=False)
    ispublic=forms.CharField(required=True)

