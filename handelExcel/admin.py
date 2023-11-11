from django.contrib import admin

# Register your models here.
from handelExcel.models import UsedCar,Car

admin.site.register(UsedCar)
admin.site.register(Car)

