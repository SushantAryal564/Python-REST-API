from django.shortcuts import render
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["POST"])
def api_home(request,*args,**kwargs):
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    # instance = serializer.save()
    print(serializer.data)
    
  # instance = Product.objects.all().order_by("?").first()
  # data = {}
  # if instance:
  #   data = ProductSerializer(instance).data
    return Response(serializer.data)
  return Response({"invalid":"not good data"},status=400)