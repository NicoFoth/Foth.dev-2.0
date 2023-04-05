from django.shortcuts import render, redirect
from .models import PokerPlayer
from .forms import UpdatePokerPlayer
from django.contrib import messages


def show_poker_page(request):

    if request.method == "POST":
        update_form = UpdatePokerPlayer(request.POST)
        
        if update_form.is_valid():
            if "deposit" in request.POST:

                name = update_form.cleaned_data["player"]
                amount = int(update_form.cleaned_data["amount"])

                queryset = PokerPlayer.objects.filter(name=name)
                current_balance = queryset[0].balance
                PokerPlayer.objects.filter(name=name).update(balance=current_balance+amount)

                return redirect("show_poker_page")


            elif "withdraw" in request.POST:

                name = update_form.cleaned_data["player"]
                amount = int(update_form.cleaned_data["amount"])

                queryset = PokerPlayer.objects.filter(name=name)
                current_balance = queryset[0].balance
                PokerPlayer.objects.filter(name=name).update(balance=current_balance-amount)

                return redirect("show_poker_page")

    else:

        update_form = UpdatePokerPlayer()
        player_data = PokerPlayer.objects.order_by("-balance")

        return render(request, "poker/show_poker_page.html", {"player_data": player_data, "update_form": update_form})
