from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name="home"),
    path('perform_action', views.perform_action, name="perform_action"),
    path('undo_action', views.undo_action, name="undo_action"),
]
