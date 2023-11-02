from django import forms
from . models import vehicles

class vehicleform(forms.ModelForm):
    class Meta:
        model=vehicles
        fields=['image','company','price','features']