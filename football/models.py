from django.db import models

# Create your models here.
class PlayerDetails(models.Model):
    country = models.CharField(max_length=60, default='UK')
    league_name = models.CharField(max_length=60, default='EPL')
    team_name = models.CharField(max_length=60, default='')
    player_name = models.CharField(max_length=60, default='')
    player_age = models.CharField(max_length=60, default='')
    position = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.player_name