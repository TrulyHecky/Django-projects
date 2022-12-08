from django.forms import ModelForm
from django import forms
from .models import Todo

class TodoForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    goal = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    completed = forms.BooleanField(required=False)
    class Meta:
        model = Todo
        fields = "__all__"