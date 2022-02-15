from django import forms


class DetectObjectForm(forms.Form):
    file = forms.FileField()