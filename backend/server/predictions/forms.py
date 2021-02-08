from django import forms
from django.core import validators


class UploadImageForm(forms.Form):
    image = forms.ImageField(validators=[validators.FileExtensionValidator(['jpg', 'jpeg'])])
