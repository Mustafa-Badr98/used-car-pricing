

from django.urls import path
# from students.api.views import hello_world, index, student_resource

# from students.api.student_views import  student_list
from handelExcel.api.views import used_cars_list,get_predicted_price
urlpatterns = [
    # path('hello', hello_world,name='api.hello_world'),
    # path('', index, name='students.api.index'),
    # path('<int:id>',student_resource, name='students.api.resource'),
    path('all_used_cars/', used_cars_list, name='used_car.models.list'),
    path('predicted_price/',get_predicted_price,name='used_car.predict.price')
]