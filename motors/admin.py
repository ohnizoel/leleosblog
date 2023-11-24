from django.contrib import admin

# Register your models here.
from .models import Motor, Rocket, Comment, Category

admin.site.register(Motor)
admin.site.register(Rocket)
admin.site.register(Comment)
admin.site.register(Category)