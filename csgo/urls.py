from django.urls import path

from . import views

urlpatterns=[
    path('', views.cs_overview, name="cs_overview"),
    path('select-players', views.select_players, name="cs_select_players"),
    path('seasons/<str:season_id>', views.season_overview, name="cs_season_overview"),
    path('matches/<str:match_id>', views.match_overview, name="cs_match_overview"),
    path('players/<str:player_id>', views.player_profile, name="cs_player_profile"),
]
