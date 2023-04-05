from django.urls import path

from . import views

urlpatterns =[
    path('', views.show_poker_page, name="show_poker_page")
]