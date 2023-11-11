from handelExcel.models import Car
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UsedCarForm

from django.shortcuts import render
from .models import UsedCar
from handelExcel.utils import calculate_final_price  # Import your utility function


def get_cars(request):
    filtered_cars=Car.objects.filter(price__lt=100000)
    filter2=filtered_cars.filter(year=2021)
    for car in filter2:
        print(car)
        
    return HttpResponse(filter2)





def calculate_price_view(request, car_id):
    used_car={}
    
    # Assuming you have a URL parameter 'car_id' to identify the car
    try:
        used_car = UsedCar.objects.get(id=car_id)
        print(used_car)
        
    except UsedCar.DoesNotExist:
        
        print(used_car)
        return render(request, 'result.html')

    # Calculate the final price using your utility function
    final_price = calculate_final_price(used_car)

    # You can pass 'final_price' to the template or use it as needed
    context = {'final_price': final_price, 'used_car': used_car}
    return render(request, 'result.html', context)
