from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.Locations.serializers import AddressSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .coordinates import find_coordinates
# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

@csrf_exempt
@api_view(['GET', 'POST'])
def address_api_view(request):
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        address_serializer = AddressSerializer(data=json_data)
        if address_serializer.is_valid(raise_exception=True):
            response = find_coordinates(address_serializer.data)

            return Response([response], status=status.HTTP_200_OK)
        else:
            return Response(address_serializer.errors)


# class AddressAPIView(APIView):
#
#
#     def post(self, request, *args, **kwargs):
#         print("hii")
#         stream = io.BytesIO(bytes(request))
#         print("s", stream)
#         json_data = JSONParser().parse(stream)
#
#         print("j", json_data)
#         address_serializer = AddressSerializer(data=json_data)
#         if address_serializer.is_valid():
#             print(address_serializer)
#             return Response(address_serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(address_serializer.errors)
#         # except:
#         #     pass
