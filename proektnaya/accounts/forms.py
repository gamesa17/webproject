from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.CharField()
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #phone = forms.CharField()

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField()
    email = forms.CharField()
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #phone = forms.CharField()

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')