from django.contrib import admin

# Register your models here.
from .models import Motor, Rocket

admin.site.register(Motor)
admin.site.register(Rocket)