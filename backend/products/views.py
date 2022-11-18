from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
class ProductListCreateAPIVIiew(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    #print(serializer.validated_data)
    title = serializer.validated_data.get("title")
    content = serializer.validated_data.get("content") or None
    if content is None:
      content = title
    serializer.save(content = content)
    # Send a Django Signal
product_list_create_view = ProductListCreateAPIVIiew.as_view()

# class ProductCreateAPIVIiew(generics.CreateAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
  
#   def perform_create(self, serializer):
#     # serializer.save(user=self.request.user)
#     #print(serializer.validated_data)
#     title = serializer.validated_data.get("title")
#     content = serializer.validated_data.get("content") or None
#     if content is None:
#       content = title
#     serializer.save(content = content)
#     # Send a Django Signal

# product_create_view = ProductCreateAPIVIiew.as_view()
  
class ProductDetailAPIVIEW(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
product_detail_view = ProductDetailAPIVIEW.as_view()

class ProductListAPIVIEW(generics.ListAPIView):
  
  """
  Not gonna use this method
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
product_list_detail_view = ProductListAPIVIEW.as_view()
@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
  method = request.method
  if method == "GET":
    if pk is not None:
      obj = get_object_or_404(Product,pk=pk)
      data = ProductSerializer(obj,many=False)
      return Response(data.data)
  
    queryset = Product.objects.all()
    data = ProductSerializer(queryset,many=True).data
    return Response(data)
    
    
  if method == "POST":
    # create a item
      serializer = ProductSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
          content = title
        serializer.save(content = content)
        return Response(serializer.data)
      return Response({"invalid":"not good data"},status=400)