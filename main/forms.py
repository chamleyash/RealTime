from django import forms
from .models import Team, Teammate

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'team_leader_name', 'team_leader_id', 'team_leader_email']

class TeammateForm(forms.ModelForm):
    class Meta:
        model = Teammate
        fields = ['name']
