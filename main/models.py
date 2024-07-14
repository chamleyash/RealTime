from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_leader_name = models.CharField(max_length=100)
    team_leader_email = models.EmailField()
    team_leader_id = models.CharField(max_length=100)
    game_name = models.CharField(max_length=100)  # Add this line

    def __str__(self):
        return self.team_leader_name

class Teammate(models.Model):
    team = models.ForeignKey(Team, related_name='teammates', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
