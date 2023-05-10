from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer, ThirdPlaceUserSerializer, ThirdPlaceUserPutSerializer
from .models import Location, ThirdPlaceUser


def index(request):
    return HttpResponse("Hello, world!")


@api_view(['GET'])
def location_list(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def location_detail(request, pk):
    try:
        user = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(user)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def third_place_user_list(request):
    if request.method == 'GET':
        users = ThirdPlaceUser.objects.all()
        serializer = ThirdPlaceUserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ThirdPlaceUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def third_place_user_detail(request, pk):
    try:
        user = ThirdPlaceUser.objects.get(pk=pk)
    except ThirdPlaceUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ThirdPlaceUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ThirdPlaceUserPutSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

