from django.shortcuts import render, redirect
from .forms import TeamForm, TeammateForm
from .models import Team, Teammate
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def tournament(request):
    return render(request, 'Tournament.html')

def register(request):
    if request.method == 'POST':
        tean_name = request.POST['teamName']
        team_leader_name = request.POST['teamLeaderName']
        team_leader_email = request.POST['teamLeaderEmail']
        team_leader_id = request.POST['teamLeaderID']
        game_name = request.POST['gameName']  # Get the game name from the form

        new_team = Team(
            team_leader_name=team_leader_name,
            team_leader_email=team_leader_email,
            team_leader_id=team_leader_id,
            game_name=game_name  # Save the game name
        )
        new_team.save()

        send_mail(
            'Registration Confirmation',
            f'Thank you for registering, {team_leader_name}. You have registered for the {game_name} tournament.
            \n\nBest regards,\nTournament Team',
            'officialaceesports1@gmail.com',
            [team_leader_email],
            fail_silently=False,
        )
        
        return redirect('success')
    return render(request, 'register.html')
def success(request):
    return render(request, 'success.html')
