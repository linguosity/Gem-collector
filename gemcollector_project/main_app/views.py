from django.shortcuts import render
from django.http import HttpResponse

gems = [
    {"name": "Azurmidas", "price": "1500 USD", "description": "A deep blue gem that shimmers with a golden core.", "weight": "5 grams", "scientific_name": "Azurea Aurum", "geotag_location": "Andes Mountains, Peru"},
    {"name": "Fire Opal", "price": "1200 USD", "description": "A vibrant, translucent gem that glows with fiery colors.", "weight": "3 grams", "scientific_name": "Opalus Ignis", "geotag_location": "Magdalena, Mexico"},
    {"name": "Shadow Quartz", "price": "980 USD", "description": "A smoky quartz that absorbs light, cloaking it in darkness.", "weight": "6 grams", "scientific_name": "Quartz Obscurum", "geotag_location": "Ural Mountains, Russia"},
    {"name": "Celestial Sapphire", "price": "2100 USD", "description": "A sapphire that reflects the night sky, complete with moving constellations.", "weight": "4 grams", "scientific_name": "Sapphirum Coelum", "geotag_location": "Kashmir, India"},
    {"name": "Emerald of the Serpent", "price": "3300 USD", "description": "An emerald that shifts in color from green to deep red as if alive.", "weight": "5 grams", "scientific_name": "Serpens Viridis", "geotag_location": "Cleopatra's Mines, Egypt"},
    {"name": "Frost Diamond", "price": "5000 USD", "description": "A diamond that perpetually exudes a chilling mist, cooling the air around it.", "weight": "2 grams", "scientific_name": "Diamond Gelu", "geotag_location": "Yakutia, Siberia"},
    {"name": "Lunar Pearl", "price": "890 USD", "description": "A pearl that glows softly in the moonlight, with a lustrous silver sheen.", "weight": "1 gram", "scientific_name": "Pearl Lunaris", "geotag_location": "Coast of Japan"},
    {"name": "Phoenix Ruby", "price": "4600 USD", "description": "A ruby that holds a flickering flame within, never extinguishing.", "weight": "3 grams", "scientific_name": "Rubinus Phoenix", "geotag_location": "Mount Vesuvius, Italy"},
    {"name": "Ethereal Amethyst", "price": "1100 USD", "description": "An amethyst with a translucent quality that seems to phase in and out of existence.", "weight": "4 grams", "scientific_name": "Amethystum Aether", "geotag_location": "Minas Gerais, Brazil"},
    {"name": "Echo Opal", "price": "760 USD", "description": "An opal that whispers echoes of words once spoken near it, holding secrets of the past.", "weight": "3 grams", "scientific_name": "Opalus Echo", "geotag_location": "Coober Pedy, Australia"}
]

# Create your views here.
def home(request):
    return render(request, 'gems/home.html')

def about(request):
    return render(request, 'gems/about.html')

def gems_index(request):
    return render(request, 'gems/index.html', {
        'gems': gems
    })