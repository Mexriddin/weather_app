from django.forms import ModelForm, TextInput
from .models import	City

class CityForm(ModelForm):
	class Meta:
		model = City
		fields = ["name"]
		widgets = {'name':TextInput(attrs={
			'class':'form-control',
			'name':'city', 
			'placeholder':'Enter city names',
			'id':'city'})}