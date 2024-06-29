from django.db import models


# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    dietary_preferences = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    health_goals = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
