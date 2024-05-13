from django import forms
from .models import Gem, Jewelry

class GemForm(forms.ModelForm):
    class Meta:
        model = Gem
        fields = ['name', 'scientific_name', 'price', 'description', 'weight', 'geotag_location', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'scientific_name': forms.TextInput(attrs={'class':'input'}),
            'price': forms.NumberInput(attrs={'class':'input'}),
            'description': forms.Textarea(attrs={'class':'textarea'}),
            'weight': forms.NumberInput(attrs={'class':'input'}),
            'geotag_location': forms.TextInput(attrs={'class':'input'}),
            'url': forms.TextInput(attrs={'class': 'input'}),
        }

class JewelryForm(forms.ModelForm):
    class Meta:
        model = Jewelry
        fields = ['name', 'price', 'url', 'description', 'type']  # Confirm these are all the fields you need
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'price': forms.NumberInput(attrs={'class': 'input'}),
            'url': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
            'type': forms.Select(attrs={'class': 'select'}),
        }
        print("hello")