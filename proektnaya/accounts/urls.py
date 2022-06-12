from django.urls import path

from .views import register, showprofile
from .forms import CustomUserCreationForm
from .views import user_login
from .views import editname
from .views import editemail


urlpatterns = [
    path('accounts/signup', register, name='signup'),
    path('my_profile', showprofile, name='my_profile'),
    path('accounts/login', user_login, name='login'),
    path('newname', editname , name = 'newname'),
    path('newemail', editemail, name = 'newemail')
]