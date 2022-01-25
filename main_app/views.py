from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to FinchCollector</h1>')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {'bird': bird})

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'

# birds = [
#   Bird('Lolo', 'finch', 'foul little demon', 3),
#   Bird('Sachi', 'parrot', 'diluted tortoise shell', 0),
#   Bird('Raven', 'chickadee', '3 legged bird', 4)
# ]



# admin info
# username: admin
# pass: bird