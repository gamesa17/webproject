from django.urls import path

from .views import register, showprofile, user_logout
from .forms import CustomUserCreationForm
from .views import user_login
from .views import editname
from .views import editeinf


urlpatterns = [
    path('accounts/signup', register, name='signup'),
    path('my_profile', showprofile, name='my_profile'),
    path('accounts/login', user_login, name='login'),
    path('newname', editname, name='newname'),
    path('editeinf', editeinf, name='editeinf'),
    path('logout', user_logout, name="logout")
]