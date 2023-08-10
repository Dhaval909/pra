from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'todolist': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Todo Here'})
        }
        labels = {
            'todolist':'TO DO '
        }