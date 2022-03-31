from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Form, CharField, EmailField, PasswordInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the name'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the description'
            }),
        }

class LoginForm(Form):
    username = CharField(label='Username')
    password = CharField(label="Password", widget=PasswordInput)


class RegisterForm(Form):
    username = CharField(label='Username')
    email = EmailField(label='Email')
    password = CharField(label="Password", widget=PasswordInput)