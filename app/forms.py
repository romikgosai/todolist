from django import forms
from django.forms import fields
from .models import Todo

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text','completion_date']
        widgets = {'completion_date': forms.DateInput(format=('%m/%d%Y'),attrs={'type':'date','placeholder':'completion date'}),
        'text': forms.TextInput(attrs={'type':'text','placeholder':'Your todo List'})
        }        