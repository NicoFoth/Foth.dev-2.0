from django.db import models

class PokerPlayer(models.Model):
    name = models.CharField(max_length=32)
    balance = models.IntegerField()
    history = models.TextField(max_length=512, blank=True)

    def __str__(self):
        return self.name