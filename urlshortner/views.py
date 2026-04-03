import random
import string
from django.shortcuts import render
from .serializers import UrlSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortUrl
from django.shortcuts import get_object_or_404,redirect
from drf_spectacular.utils import extend_schema

def generateshortcode():
    while True:
        shortcode = "".join(random.choices(string.ascii_letters+string.digits,k=6))
        if not ShortUrl.objects.filter(shortcode=shortcode).exists():
            return shortcode

class ShortenUrlView(APIView):
    @extend_schema(request=UrlSerializer,responses=UrlSerializer)
    def post(self,req):
        incomingjson = req.data
        serializer = UrlSerializer(data=incomingjson)
        if serializer.is_valid():
            shortcode = generateshortcode()
            serializer.save(shortcode = shortcode)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class RedirectView(APIView):
    def get(self,req,shortcode):
        tablerow = get_object_or_404(ShortUrl,shortcode=shortcode)
        tablerow.clickcount+=1
        tablerow.save()
        return redirect(tablerow.originalurl)
class UrlView(APIView):
    def get(self,req):
        allrows = ShortUrl.objects.all()
        serializer = UrlSerializer(allrows,many=True)
        return Response(serializer.data)





    


