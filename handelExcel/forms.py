# forms.py
from django import forms
from .models import Car
from .models import UsedCar

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'





class UsedCarForm(forms.ModelForm):
    class Meta:
        model = UsedCar
        fields = '__all__'
