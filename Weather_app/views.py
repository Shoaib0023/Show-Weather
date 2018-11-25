from django.shortcuts import render, HttpResponse, redirect
import requests
from . forms import AddCityForm
from . models import City

# Create your views here.
def home(request):
	cities = City.objects.all()
	url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=038faa6e0b9143d7a67fac87ec1be7ce"

	if request.method == "POST":
		form = AddCityForm(request.POST)
		if form.is_valid():
			form.save()

	form = AddCityForm()
	weather_data = []

	for city_name in cities:
		city = city_name
		data = requests.get(url.format(city)).json()
		weather = {
			'city': city,
			'description': data['weather'][0]['description'],
			'icon': data['weather'][0]['icon'],
			'temprature': data['main']['temp'],
			'temprature_in_celcius': str("%.2f" % (( data['main']['temp'] - 32)*0.56))
			}

		weather_data.append(weather)

	context = {
		'weather_data': weather_data,
		'form': form
	}

	return render(request, 'home.html', context)

def remove(request, pk):
	Object = City.objects.get(pk=pk)
	Object.delete()
	return redirect("home")
