from django import forms
from main.models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['hp', 'iq', 'happiness']