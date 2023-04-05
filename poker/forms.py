from django import forms
from .models import PokerPlayer

class UpdatePokerPlayer(forms.Form):

    players = PokerPlayer.objects.order_by("name")
    
    choices = []
    for player in players:
        choices.append((player, player.name))

    choices_tuple = tuple(choices)
    player = forms.ChoiceField(choices=choices_tuple)
    amount = forms.IntegerField()
    