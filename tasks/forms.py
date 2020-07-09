from django import forms
from django.forms import ModelForm
from .models import Task




class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control todo-list-input', 'placeholder':'What do you need to do today?'}))
    class Meta:
        model = Task
        fields = '__all__'
