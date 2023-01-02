from django.http import JsonResponse
from .models import Security
from .serializers import SecuritySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def security_list(request, format = None):
    if(request.method == 'GET'):
        securities = Security.objects.all()
        serializer = SecuritySerializer(securities, many = True)
        return Response(serializer.data)
    elif(request.method == 'POST'):
        serializer = SecuritySerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def security_details(request, id, format = None):

    try:
        security = Security.objects.get(pk = id)
    except Security.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if(request.method == 'GET'):
        serializer = SecuritySerializer(security)
        return Response(serializer.data)
    elif(request.method == 'PUT'):
        serializer = SecuritySerializer(security, data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif(request.method == 'DELETE'):
        security.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)