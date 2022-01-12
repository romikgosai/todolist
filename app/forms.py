from django import forms
from django.forms import fields
from .models import Todo

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text','completion_date']
        