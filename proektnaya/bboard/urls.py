from django.contrib import admin
from django.urls import path


from .views import index
from bboard.views import by_rubric
from bboard.views import CompanyView
from .views import createnew




urlpatterns = [
    path('add/', createnew, name = 'add'),
    path('<int:rubric_id>/', by_rubric, name = 'by_rubric'),
    path('', index, name = 'index'),
]