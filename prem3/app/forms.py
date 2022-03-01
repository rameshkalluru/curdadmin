from dataclasses import fields
from django import forms

from app.models import sukku

class sukku_mar(forms.ModelForm):
    class Meta:
        model='sukku'
        fields="__all__"