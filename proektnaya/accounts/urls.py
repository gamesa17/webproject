from django.urls import path

from .views import register, showprofile
from .forms import CustomUserCreationForm

urlpatterns = [
    path('accounts/signup', register, name='signup'),
    path('my_profile', showprofile, name='my_profile'),
]