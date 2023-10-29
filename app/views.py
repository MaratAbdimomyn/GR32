from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from .forms import *

class CarView(ListView):
    model = Cars
    template_name = 'home.html'
    context_object_name = 'cars'

def SearchCar(request):
    cars = []
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            hide = cd['name']
            cars = Cars.objects.filter(name=hide)

    return render(request, 'search.html', {'cars':cars, 'form':form})