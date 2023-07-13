from django.contrib import admin
from .models import *

admin.site.register(PokerPlayer)
admin.site.register(PokerSeason)
admin.site.register(PokerGame)
admin.site.register(PokerPlayerGamePerformance)