from django import forms
from alexandria_app.models import File

# stores all the file objects.
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'image']
