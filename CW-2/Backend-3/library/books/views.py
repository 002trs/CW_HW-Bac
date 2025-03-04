from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Player  # Исправлено на Player


def players(request):
    template = loader.get_template("all_players.html")
    all_players = Player.objects.all()  # Исправлено на Player
    my_context = {
        "all_players": all_players
    }
    return HttpResponse(template.render(context=my_context))

def description(request, id):
    player = Player.objects.get(id=id)  # Исправлено на Player
    template = loader.get_template("description.html")
    context = {
        "myplayer": player
    }
    return HttpResponse(template.render(context=context))