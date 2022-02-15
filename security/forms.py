from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Person
        fields = ('firstname', 'lastname', 'age', 'phone_number', 'images')

class DetectFaceForm(forms.Form):
    image = forms.ImageField()