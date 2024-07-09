from django.db import models

# Create your models here.

class Bounty(models.Model):
    name = models.CharField(max_length=100)
    energy_cost = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "bounties"
