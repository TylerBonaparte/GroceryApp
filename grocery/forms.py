# grocery/forms.py

from django import forms
from .models import Item

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity', initial=1)
    
class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']
