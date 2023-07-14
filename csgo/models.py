from django.db import models


class CSRank(models.Model):
    name = models.CharField(max_length=32, unique=True)
    imageLink = models.CharField(max_length=128)
    minElo = models.IntegerField(default=0)
    maxElo = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
    
class CSMap(models.Model):
    name = models.CharField(max_length=32, unique=True)
    
    def __str__(self):
        return f"{self.name}"
    

class CSMode(models.Model):
    name = models.CharField(max_length=32, unique=True)
    
    def __str__(self):
        return f"{self.name}"
    

class CSPlayer(models.Model):
    steam_id = models.CharField(max_length=18, unique=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"
    

class CSSeason(models.Model):
    name = models.CharField(max_length=32)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f"{self.name}"
    

class CSMatch(models.Model):
    date = models.DateTimeField()
    season = models.ForeignKey(CSSeason, on_delete=models.CASCADE)
    map = models.ForeignKey(CSMap, on_delete=models.CASCADE)
    mode = models.ForeignKey(CSMode, on_delete=models.CASCADE)
    endstate = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.date} - {self.map} - {self.endstate}"
    

class CSPlayerMatch(models.Model):
    player = models.ForeignKey(CSPlayer, on_delete=models.CASCADE)
    match = models.ForeignKey(CSMatch, on_delete=models.CASCADE)
    
    eloChange = models.FloatField(default=0)
    win = models.BooleanField(default=False)
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    headshotKills = models.IntegerField(default=0)
    mvps = models.IntegerField(default=0)
    enemiesFlashed = models.IntegerField(default=0)
    utilityDamage = models.IntegerField(default=0)

    class Meta:
        unique_together = ('player', 'match')

    def __str__(self):
        return f"{self.player} - {self.match}"
    

class CSPlayerSeasonElo(models.Model):
    player = models.ForeignKey(CSPlayer, on_delete=models.CASCADE)
    season = models.ForeignKey(CSSeason, on_delete=models.CASCADE)
    elo = models.IntegerField(default=1500)

    class Meta:
        unique_together = ('player', 'season')

    def __str__(self):
        return f"{self.player} - {self.elo}"