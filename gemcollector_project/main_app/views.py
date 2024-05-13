from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Gem, Jewelry, Toy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .forms import GemForm, JewelryForm

# Create your views here.
def home(request):
    return render(request, 'gems/home.html')

def about(request):
    return render(request, 'gems/about.html')

def gems_detail(request, gem_id):
    gem = Gem.objects.get(id=gem_id)
    toys = Toy
    id_list = gem.toys.all().values_list('id')
    print(id_list)
    jewels = gem.jewelry.all()

    toys_cat_doesnt_have = Toy.objects.exclude(id__in=id_list)
    jewelry_form = JewelryForm()

    return render(request, 'gems/detail.html', {
         'gem': gem,
         'jewels': jewels,
         'jewelry_form': jewelry_form,
        'toys': toys_cat_doesnt_have
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

def assoc_toy(request, pk, toy_pk):
  Gem.objects.get(id=pk).toys.add(toy_pk)
  return redirect('detail', gem_id=pk)

def assoc_delete(request, pk, toy_pk):
  Gem.objects.get(id=pk).toys.remove(toy_pk)
  return redirect('detail', gem_id=pk)

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

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'