from django.forms import ModelForm
from django import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import BBoard

class BBForm(ModelForm):
    class Meta:
        model = BBoard
        fields = ('title', 'content')


class BBCreateView(CreateView):
    title = forms.CharField()
    content = forms.CharField()

    class Meta(CreateView):
        model = BBoard
        fields = ('title', 'content')


