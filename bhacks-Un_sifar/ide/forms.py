from django import forms
from . import models

class code(forms.ModelForm):
    class Meta:
        model=models.code
        fields=('code_input','lang')

        