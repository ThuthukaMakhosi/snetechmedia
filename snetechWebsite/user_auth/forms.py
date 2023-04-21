from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUp(UserCreationForm):
    first_name = forms.CharField(max_length=150)

    class Meta:
        model =User
        fields = ('username', 'first_name', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }