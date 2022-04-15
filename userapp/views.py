from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import username
from .serializers import usernameserializer
from .utils import GetImageFromInstagram

@api_view(['post']) 
def username(request):
    username_data = {
       "username": request.data['username']
    }

    ser= usernameserializer(data=username_data)
    if ser.is_valid():
        ser.save()

        insta_obj=GetImageFromInstagram(username_data["username"])
        profile_img= insta_obj.get_image()
        return HttpResponse(profile_img , content_type= "image/jpeg", status=status.HTTP_200_OK)
    else:
        return Response({"Error" : "Bad Data"} , status= status.HTTP_400_BAD_REQUEST)

