from django import forms
from .models import Gem

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
            'url': forms.TextInput(attrs={'class': 'input'}),
        }

