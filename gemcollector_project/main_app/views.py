from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Gem, Jewelry
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .forms import GemForm, JewelryForm

# Create your views here.
def home(request):
    return render(request, 'gems/home.html')

def about(request):
    return render(request, 'gems/about.html')

def gems_detail(request, gem_id):
    gem = Gem.objects.get(id=gem_id)

    id_list = gem.jewelry.all().values_list('id')
    jewels = gem.jewelry.all()

    jewelry_form = JewelryForm()

    
    return render(request, 'gems/detail.html', {
         'gem': gem,
         'jewels': jewels,
         'jewelry_form': jewelry_form,
    })


def add_jewelry(request, pk):
    # create a JewelryForm instance using data in request.POST
    form = JewelryForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form until it has our gem_id assigned
        new_jewelry = form.save(commit=False)
        new_jewelry.gem_id = pk  # set the foreign key to the gem
        new_jewelry.save()  # save the new jewelry
    return redirect('detail', gem_id=pk)  # Redirect to the gem's detail page

class GemList(ListView):
    model = Gem

class GemCreate(CreateView):
    form_class = GemForm
    model = Gem

class GemUpdate(UpdateView):
    form_class = GemForm
    model = Gem

class GemDelete(DeleteView):
    model = Gem
    success_url = '/gems/'