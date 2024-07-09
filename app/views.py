from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ViewSet,ModelViewSet
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
    
    def create(self,request):
        jd=request.data
        pd=ProductMS(data=jd)
        if pd.is_valid():
            pd.save()
            return Response({'Create':'data is inserted'})
        else:
            return Response({'Failed':'not Created'})

    def update(self,request,pk):
        PRO=Product.objects.get(pid=pk)
        jd=request.data
        pd=ProductMS(PRO,data=jd)
        if pd.is_valid():
            pd.save()
            return Response({'Updated':'data is Updated'})
        else:
            return Response({'Failed':'not Updated'})
   
    def partial_update(self,request,pk):
        PRO=Product.objects.get(pid=pk)
        jd=request.data
        pd=ProductMS(PRO,data=jd,partial=True)
        if pd.is_valid():
            pd.save()
            return Response({'Updated':'data is Updated'})
        else:
            return Response({'Failed':'not Updated'})
    
    def destroy(self,request,pk):
        PRO=Product.objects.get(pid=pk)
        PRO.delete()
        return Response({'delete':'DEletion is done successfully'})



class ProductCrudBYMV(ModelViewSet):
    serializer_class=ProductMS
    queryset=Product.objects.all()







































