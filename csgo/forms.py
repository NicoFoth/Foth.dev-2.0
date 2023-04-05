from django import forms
from .models import CsgoPlayer

class SelectPlayers(forms.Form):
    selected_players = forms.ModelMultipleChoiceField(queryset=CsgoPlayer.objects.all(), widget=forms.CheckboxSelectMultiple)