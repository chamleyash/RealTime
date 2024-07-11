from django.shortcuts import render, redirect
from .forms import TeamForm, TeammateForm
from .models import Team, Teammate

def index(request):
    return render(request, 'index.html')

def tournament(request):
    return render(request, 'Tournament.html')

from django.shortcuts import render, redirect
from .forms import TeamForm
from .models import Team, Teammate

def register(request):
    if request.method == 'POST':
        print(request.POST)  # Debugging line

        team_leader_name = request.POST.get('teamLeaderName')
        team_leader_email = request.POST.get('teamLeaderEmail')
        team_leader_id = request.POST.get('teamLeaderID')

        team = Team(
            team_name=team_leader_name,  # You might want to change this if team name is different
            team_leader_name=team_leader_name,
            team_leader_email=team_leader_email,
            team_leader_id=team_leader_id
        )
        team.save()

        for i in range(1, 6):  # Assuming a maximum of 5 teammates
            teammate_name = request.POST.get(f'teammate{i}Name')
            if teammate_name:
                Teammate.objects.create(team=team, name=teammate_name)

        return redirect('success')  # Change this to your success URL name or view
    return render(request, 'register.html')
def success(request):
    return render(request, 'success.html')
