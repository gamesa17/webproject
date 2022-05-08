from django.urls import path

from .views import register, showprofile

urlpatterns = [
    path('signup/', register, name='signup'),
    path('my_profile', showprofile, name='my_profile')
]