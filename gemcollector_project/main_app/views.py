from django.shortcuts import render
#from django.http import HttpResponse
from .models import Gem
from django.views.generic import ListView,CreateView,DeleteView,UpdateView

# Create your views here.
def home(request):
    return render(request, 'gems/home.html')

def about(request):
    return render(request, 'gems/about.html')

def gems_detail(request, gem_id):
    gem = Gem.objects.get(id=gem_id)
    return render(request, 'gems/detail.html', { 'gem': gem})

class GemList(ListView):
    model = Gem

class GemCreate(CreateView):
    model = Gem
    fields = ['name', 'description']

class GemUpdate(UpdateView):
    model = Gem
    fields = ['name', 'description']

class GemDelete(DeleteView):
    model = Gem
    success_url = '/gems/'