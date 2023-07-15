from django.urls import path

from . import views

urlpatterns=[
    path('', views.cs_overview, name="cs_overview"),
    path('select-players', views.select_players, name="select_players"),
    path('seasons/<str:season_id>', views.season_overview, name="season_overview"),
]
