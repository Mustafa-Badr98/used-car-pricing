
from rest_framework import serializers

from handelExcel.models import UsedCar 

class UsedCarModelSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = UsedCar
        fields = '__all__'