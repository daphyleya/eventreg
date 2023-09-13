from django import forms
from .models import read

class readforms(forms.ModelForm):
    class Meta:
        model=read
        fields=['name','email','phone']