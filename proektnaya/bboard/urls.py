from django.contrib import admin
from django.urls import path


from .views import index, details
from bboard.views import by_rubric
from .views import createnew
from django.contrib.auth import views as authViews




urlpatterns = [
    path('add/', createnew, name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('details/<int:id>/', details, name='details'),
    path('exit/', authViews.LogoutView.as_view(next_page="{% url 'auth' %}"), name='exit'),
]