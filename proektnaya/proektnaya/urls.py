"""proektnaya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from bboard.views import index
from bboard.views import CompanyView
from bboard.views import auth
from accounts.views import register
from accounts.views import showprofile
from bboard.views import login_user
#from bboard.views import BBoardLoginView, BBoardRegUser
from bboard.views import profile
from bboard.views import adcreate
from bboard.views import createnew

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/company/<int:id>', CompanyView, name='company'),
    path('auth/', auth, name = 'auth'),
    path('profile/', profile, name = 'profile'),
    path('', include("accounts.urls")),
    #path('addcreate/add', createnew, name = 'add'),
    path('', include('bboard.urls')),
    path('adcreate/', adcreate, name = 'adcreate')
]
