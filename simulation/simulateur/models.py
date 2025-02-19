from django.db import models

# Create your models here.
class Animal(models.Model):
    nom = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.nom