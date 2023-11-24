from django import forms
from django.forms import ModelForm
from .models import Motor, Comment

class MotorForm(ModelForm):
    class Meta:
        model = Motor
        fields = [
            'name',
            'launch_year',
            'specific_impulse',
            'thrust',
            'mass',
            'burn_time',
            'propellant',
            'motor_image',
        ]
        labels = {
            'name': 'Nome',
            'launch_year': 'Data de Lançamento',
            'specific_impulse': 'Impulso específico',
            'thrust': 'Impulso total',
            'mass': 'Massa',
            'burn_time': 'Tempo de queima',
            'propellant': 'Propelente',
            'motor_image': 'Imagem do Motor',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Autor',
            'text': 'Comentário',
        }