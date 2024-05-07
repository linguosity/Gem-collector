from django.shortcuts import render
#from django.http import HttpResponse
from .models import Gem, Jewelry
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .forms import GemForm

# Create your views here.
def home(request):
    return render(request, 'gems/home.html')

def about(request):
    return render(request, 'gems/about.html')

def gems_detail(request, gem_id):
    gem = Gem.objects.get(id=gem_id)
    #jewels = Jewelry

    id_list = gem.jewelry.all().values_list('id')
    jewels = gem.jewelry.all()
    
    return render(request, 'gems/detail.html', {
         'gem': gem,
         'jewels': jewels
    })

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