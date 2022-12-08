from django import forms
from .models import Converter
from ckeditor.widgets import CKEditorWidget

class ConverterForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label="Enter text down below:")

    class Meta:
        model = Converter
        fields = "__all__"