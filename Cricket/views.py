from django.shortcuts import render, redirect
from .models import ttwenty_team, test_match

# Create your views here.
def players(request):
    team = ttwenty_team.objects.all()
    return render(request, 'players_list.html', {'team': team})

def players_two(request):
    teams = test_match.objects.all()
    return render(request, 'players_two.html', {'teams': teams})


def add_players(request):
    if request.method == "GET":
        return render(request, 'add.html')
    else:
        ttwenty_team (
            firstname = request.POST.get('fname'),
            lastname = request.POST.get('lname'),
            talent = request.POST.get('tlent'),
            score = request.POST.get('score')
        ) .save()
        return render(request, 'players_list.html')

def add_players_two(request):
    if request.method == "GET":
        return render(request, 'add2.html')
    else:
        test_match (
            firstname = request.POST.get('f_name'),
            lastname = request.POST.get('l_name'),
            talent = request.POST.get('t_lent'),
            score = request.POST.get('s_core')
        ) .save()
        return render(request, 'players_two.html')
    
    
def update_players(request, pk):
    player = ttwenty_team.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'update.html', {'player': player})
    else:
        player.firstname = request.POST.get('fname')
        player.lastname = request.POST.get('lname')
        player.talent = request.POST.get('tlent')
        player.score = request.POST.get('score')
        player.save()
        return redirect('home')
    
    
def update_players_two(request, pk):    
    players = test_match.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'update2.html', {'players': players})
    else:
        players.firstname = request.POST.get('f_name')
        players.lastname = request.POST.get('l_name')
        players.talent = request.POST.get('t_lent')
        players.score = request.POST.get('s_core')
        players.save()
        return redirect('home_two')
 
def delete_players(request, pk):
    team = ttwenty_team.objects.get(pk=pk)
    if request.method == "GET":
        team.delete()
        return redirect('home')
    
def delete_players_two(request, pk):
    teams = test_match.objects.get(pk=pk)
    if request.method == "GET":
        teams.delete()
        return redirect('home_two')    
            
               
    
        