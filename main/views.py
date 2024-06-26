from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def tournament(request):
    return render(request, 'Tournament.html')

def register(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST)
        if team_form.is_valid():
            team = team_form.save()
            for i in range(1, 6):
                teammate_name = request.POST.get(f'teammate{i}Name')
                if teammate_name:
                    Teammate.objects.create(team=team, name=teammate_name)
            return redirect('success')
    else:
        team_form = TeamForm()
    return render(request, 'register.html', {'team_form': team_form})

def success(request):
    return render(request, 'success.html')
