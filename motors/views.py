from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Motor, Comment, Category
from .forms import MotorForm, CommentForm
from django.views import generic
from django.urls import reverse
from django.urls import reverse_lazy

#def detail_motor(request, motor_id):
#    context = {'motor': motor_data[motor_id - 1]}
#    return render(request, 'motors/detail.html', context)
class MotorDetailView(generic.DetailView):
    model = Motor
    template_name = 'motors/detail.html'

class MotorListView(generic.ListView):
    model = Motor
    template_name = 'motors/index.html'

def search_motors(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        motor_list = Motor.objects.filter(name__icontains=search_term)
        context = {"motor_list": motor_list}
    return render(request, 'motors/search.html', context)


def create_motor(request):
    if request.method == 'POST':
        form = MotorForm(request.POST, request.FILES)
        if form.is_valid():
            motor_name = form.cleaned_data['name']
            motor_launch_year = form.cleaned_data['launch_year']
            motor_specific_impulse = form.cleaned_data['specific_impulse']
            motor_thrust = form.cleaned_data['thrust']
            motor_mass = form.cleaned_data['mass']
            motor_burn_time = form.cleaned_data['burn_time']
            motor_propellant = form.cleaned_data['propellant']
            motor_motor_image = form.cleaned_data['motor_image']
            motor = Motor(name=motor_name,
                        launch_year=motor_launch_year,
                        specific_impulse=motor_specific_impulse,
                        thrust=motor_thrust,mass=motor_mass,
                        burn_time=motor_burn_time,propellant=motor_propellant,motor_image=motor_motor_image)
            motor.save()
            return HttpResponseRedirect(
                reverse('motors:detail', args=(motor.id, )))
    else:
        form = MotorForm()
        context = {'form': form}
        return render(request, 'motors/create.html', context)

def update_motor(request, pk):
    motor = get_object_or_404(Motor, pk=pk)
    if request.method == "POST":
        form = MotorForm(request.POST, request.FILES)
        if form.is_valid():
            motor.name = form.cleaned_data['name']
            motor.launch_year = form.cleaned_data['launch_year']
            motor.specific_impulse = form.cleaned_data['specific_impulse']
            motor.thrust = form.cleaned_data['thrust']
            motor.mass = form.cleaned_data['mass']
            motor.burn_time = form.cleaned_data['burn_time']
            motor.propellant = form.cleaned_data['propellant']
            motor.motor_image = form.cleaned_data['motor_image']
            motor.save()
            return HttpResponseRedirect(
                reverse('motors:detail', args=(motor.id, )))

    else:
        form = MotorForm(
            initial={
                'name': motor.name,
                'launch_year': motor.launch_year,
                'specific_impulse': motor.specific_impulse,
                'thrust': motor.thrust,
                'mass': motor.mass,
                'burn_time': motor.burn_time,
                'propellant': motor.propellant,
                'motor_image': motor.motor_image
            })
    
    context = {'motor': motor, 'form': form}
    return render(request, 'motors/update.html', context)


def delete_motor(request, pk):
    motor = get_object_or_404(Motor, pk=pk)

    if request.method == "POST":
        motor.delete()
        return HttpResponseRedirect(reverse('motors:index'))

    context = {'motor': motor}
    return render(request, 'motors/delete.html', context)

def create_comment(request, pk):
    motor = get_object_or_404(Motor, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            motor=motor)
            comment.save()
            return HttpResponseRedirect(
                reverse('motors:detail', args=(pk, )))
    else:
        form = CommentForm()
    context = {'form': form, 'motor': motor}
    return render(request, 'motors/comment.html', context)

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'motors/category.html'


class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = 'motors/create_category.html'
    fields = ['name', 'motors']
    success_url = reverse_lazy('motors:category')

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'motors/category_detail.html'