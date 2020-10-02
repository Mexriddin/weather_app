from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import	City
from .forms import	CityForm
import requests
from django.contrib import messages
# Create your views here.

def index(request):
	key="ac95b4f4831d2b591d227ab1097511cf"
	url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + key

	if request.method == "POST":
		form = CityForm(request.POST)
		if form.is_valid():
			form.save()

	form = CityForm()

	cities = City.objects.all()
	all_cities = []

	for city in cities:
		res = requests.get(url.format(city.name.title())).json()
		if res.get("main") is not None:
			city_info = {
					'city':city.name.title(),
					"temp":res.get("main")["temp"],
					"speed":res.get("wind")["speed"],
					"icon":res.get("weather")[0]["icon"]
			}
			all_cities.append(city_info)
		else:
			messages.warning(request,'City name is incorrect')

	context = {"all_info":all_cities[::-1], "form":form}
	return render(request,"weather/index.html",context)

def clear(request):
	if request.method == 'POST':
		City.objects.all().delete()
		return redirect('index')
	return render(request, 'weather/confirm_clear.html')
    # success_url ="/"