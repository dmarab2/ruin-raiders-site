from django.db import models

# Create your models here.

class Bounty(models.Model):
    name = models.CharField(max_length=100)
    energy_cost = models.IntegerField()
    description = models.TextField()

    def __str__():
        return self.name
