from django.db import models
from django.conf import settings

# Create your models here.
class Motor(models.Model):
    name = models.CharField(max_length=255)
    launch_year = models.IntegerField()
    specific_impulse = models.FloatField()
    thrust = models.FloatField()
    mass = models.FloatField()
    burn_time = models.FloatField()
    propellant = models.CharField(max_length=255)
    poster_url = models.CharField(max_length=200, null=True)
    motor_image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return f'{self.name} ({self.launch_year}) {self.specific_impulse} {self.thrust} {self.mass} {self.burn_time} {self.propellant}'

class Rocket(models.Model):
    rocket = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    sucessfull_static_tests = models.IntegerField(default=0)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'"{self.text}" - {self.rocket.username}'