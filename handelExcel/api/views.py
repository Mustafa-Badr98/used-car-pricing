
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.decorators import  api_view
from handelExcel.models import UsedCar
from handelExcel.api.serializers import UsedCarModelSerializer
from handelExcel.utils import calculate_final_price
from types import SimpleNamespace



@api_view(['GET'])
def used_cars_list(request):
    if request.method == 'GET':
        used_cars = UsedCar.get_all_usedCars()
        serialized_used_car = UsedCarModelSerializer(used_cars, many=True)
        return Response({"data":serialized_used_car.data}, status=status.HTTP_200_OK)

    else:
        return Response({"message":"Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)






@api_view(['POST'])
def get_predicted_price(request):
        if request.method == 'POST':
            serialized_used_car = UsedCarModelSerializer(data = request.data)
        
            if serialized_used_car.is_valid():
                # serialized_used_car.save()
                print(serialized_used_car.validated_data)
                ordered_dict_data = serialized_used_car.validated_data
                used_car_object = SimpleNamespace(**ordered_dict_data)
                print(used_car_object)
                final_price = calculate_final_price(used_car_object)
                print(final_price)
                return Response({"predicted_price":final_price}, status=status.HTTP_201_CREATED)
            return Response({"error":serialized_used_car.errors}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"message":"Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)