from django import forms
from django.forms import CharField
from .models import Registration


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(min_length=5, max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    password = forms.CharField(min_length=8, max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = Registration
        fields = ['username', 'password']
