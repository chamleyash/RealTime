from django.db import models

class Team(models.Model):
    team_leader_name = models.CharField(max_length=100)
    team_leader_email = models.EmailField()
    team_leader_id = models.CharField(max_length=100)

class Teammate(models.Model):
    team = models.ForeignKey(Team, related_name='teammates', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
