from django.forms import ModelForm

from .models import BBoard

class BBForm(ModelForm):
    class Meta:
        model = BBoard
        fields = ('title', 'content', 'price', 'rubric')