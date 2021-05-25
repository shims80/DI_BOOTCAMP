from django.shortcuts import render
from .models import Family, Animal
# Create your views here.

def al_animals(request):
    animals = Animal.objects.all()
    return render(request,'all_animals.html', {'all_animals':animals})
