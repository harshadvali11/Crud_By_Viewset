from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ViewSet
from app.models import *

from app.serializers import *
from rest_framework.response import Response

class ProductCrudView(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()
        JPO=ProductMS(LPO,many=True)
        return Response(JPO.data)
    
    def retrieve(self,request,pk):
        PO=Product.objects.get(pid=pk)
        JO=ProductMS(PO)
        return Response(JO.data)










