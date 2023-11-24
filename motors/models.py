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
    motor_image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return f'{self.name} ({self.launch_year}) {self.specific_impulse} {self.thrust} {self.mass} {self.burn_time} {self.propellant}'

class Rocket(models.Model):
    rocket = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    sucessfull_static_tests = models.IntegerField(default=0)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f'"{self.text}" - {self.rocket.username}'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    motors = models.ManyToManyField(Motor)

    def __str__(self):
        return f'{self.name}'