from django import forms
from .models import *

class SelectPlayers(forms.Form):
    #selected_players = forms.ModelMultipleChoiceField(queryset=CsgoPlayer.objects.all(), widget=forms.CheckboxSelectMultiple)
    pass