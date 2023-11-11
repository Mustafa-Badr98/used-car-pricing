from django.urls import path,include
from handelExcel.views import get_cars
from handelExcel.views import calculate_price_view
urlpatterns = [
    path('',get_cars,name='get_cars'),
    path('predict_price/<int:car_id>', calculate_price_view, name='predict_price'),
    path('api/', include("handelExcel.api.urls"))
    
    
]
