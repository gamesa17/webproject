from django.forms import ModelForm, TextInput
from django import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import BBoard, Request


class BBForm(ModelForm):
    class Meta:
        model = BBoard
        fields = ('title', 'content')


class BBCreateView(ModelForm):
    title = forms.CharField()
    content = forms.CharField()

    class Meta(ModelForm):
        model = BBoard
        fields = ('title', 'content')
        exclude = ('author',)


class MakeReqForm(ModelForm):
    class Meta:
        model = Request
        # fields = ["author_name"]
        exclude = ("author", "author_name", "response",)
        # widgets = {
        #     "author_name": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Введите название'
        #     })
        # }


class AcceptReqForm(ModelForm):
    response = forms.NullBooleanField()

    class Meta:
        model = Request
        exclude = ("author", "author_name", "response")


