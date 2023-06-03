from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from customer.serializers import *

# Create your views here.

class GetcustomerViews(APIView):

    def get(self,request):

        instance=customer.objects.all()
        serializer=GetcustomerSerializer(instance,many=True)
        return Response (serializer.data)
    
    def post(self,request):
        
        params=request.data
        print("data",params)
        serializers=GetcustomerSerializer(data=params)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(("massage","Save Sucessfully"))
    
class CustomerAdressViews(APIView):
    
    def get(self,request):
        instance=customer.object.all()
        serializer=CustomeradressSerializer(instance,many=True)
        return Response(serializer.data)
    
class CustomerDetailsAddressViews(APIView):

    def get(self,request,pk):
        instance=customer.object.filter(id=pk)
        serializers=CustomerDetailsAddressSerializer(instance,many = True)
        return Response(serializers.data)
    
