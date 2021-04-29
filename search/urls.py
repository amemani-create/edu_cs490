from django.urls import path
from . import views

urlpatterns = [
    path('', views.customSearch, name='custom_search'),
]