from django.urls import path

from . import views

urlpatterns =[
    path('', views.show_projects, name="show_projects")
]