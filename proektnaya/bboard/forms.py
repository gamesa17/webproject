from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import BBoard

class BBForm(ModelForm):
    class Meta:
        model = BBoard
        fields = ('title', 'content', 'price', 'rubric')


class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegUserForm():
    class Meta:
        model = User
        fields = ('username', 'password')
