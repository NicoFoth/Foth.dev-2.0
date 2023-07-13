from django.db import models

class PokerPlayer(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    

class PokerSeason(models.Model):
    name = models.CharField(max_length=32)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class PokerGame(models.Model):
    date = models.DateField()
    season = models.ForeignKey(PokerSeason, on_delete=models.CASCADE)

    def __str__(self):
        return "Pokergame: "  + str(self.date)


class PokerPlayerGamePerformance(models.Model):
    player = models.ForeignKey(PokerPlayer, on_delete=models.CASCADE)
    game = models.ForeignKey(PokerGame, on_delete=models.CASCADE)
    chips = models.IntegerField()

    def __str__(self):
        return str(self.player) + str(self.game)