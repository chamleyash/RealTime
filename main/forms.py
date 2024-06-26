from django import forms
from .models import Team, Teammate

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_leader_name', 'team_leader_email', 'team_leader_id']

class TeammateForm(forms.ModelForm):
    class Meta:
        model = Teammate
        fields = ['name']
