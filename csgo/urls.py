from django.urls import path

from . import views

urlpatterns=[
    path('', views.show_csgo_stats, name="show_csgo_stats"),
    path('select-players', views.select_players, name="select_players"),
    path('<str:steam_id>', views.player_profile, name="player_profile")
]
