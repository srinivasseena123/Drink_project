from django.http import JsonResponse
from .models import Drink
from .serialzers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pdb;


# Create your views here.
# We create all endpoints

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    # Get all the drinks
    # Serialize them
    # Return JSON

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks': serializer.data})
    

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            pdb.set_trace()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
       
    if request.method == 'GET':
        serialzer = DrinkSerializer(drink)
        return Response(serialzer.data)
    elif request.methodb == 'PUT':
        serialzer = DrinkSerializer(drink, data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
