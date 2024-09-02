from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Products
from api.serializers import Productserializers

class ProductView(APIView):
    def get(self,request,*args,**kw):
       qs=Products.objects.all()
       serializer=Productserializers(qs,many=True)
       return Response(data=serializer.data)
    
    def post(self,request,*args,**kw):
        serializer=Productserializers(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
class ProductdetailView(APIView):
    def get(self,request,*arg,**kw):
        return Response(data='detail of product')
    def post(self,request,*arg,**kw):
        return Response(data='item sucessfully apdated')
    def delete(self,request,*arg,**kw):
        return Response(data='item deleted')