from django import forms

from .models import Account

class SignUpForm(forms.ModelForm):
    class Meta:
        model=Account