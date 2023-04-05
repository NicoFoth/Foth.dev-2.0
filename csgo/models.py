from django.db import models

class CsgoPlayer(models.Model):
    steam_id = models.CharField(max_length=18)
    name = models.CharField(max_length=32)
    elo = models.IntegerField(default=1500)

    kills = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    played_matches = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"