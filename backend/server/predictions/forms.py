from django import forms
from django.core import validators


class UploadImageForm(forms.Form):
    image = forms.ImageField(label='Select an image file',
                             help_text='Max is 10 megabytes',
                             validators=[validators.FileExtensionValidator(['jpg', 'jpeg'])])
