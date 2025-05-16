from django import forms
from todo.models import *

class TodoForm(forms.ModelForm):
    class Meta:
        model=TodoList
        fields='__all__'