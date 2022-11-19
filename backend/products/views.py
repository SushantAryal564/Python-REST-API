from rest_framework import generics,mixins;
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
  #lookup_field = "pk"
  
product_detail_view = ProductDetailAPIVIEW.as_view()

class ProductUpdateAPIVIEW(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_update(self,serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title
  
product_update_view = ProductUpdateAPIVIEW.as_view()

class ProductDeleteAPIVIEW(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_destroy(self,instance):
    #instance
    super().perform_destroy(instance)
  
product_delete_view = ProductDeleteAPIVIEW.as_view()

class ProductListAPIVIEW(generics.ListAPIView):
  
  """
  Not gonna use this method
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
product_list_detail_view = ProductListAPIVIEW.as_view()

class ProductMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,generics.GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  def get(self,request,*args,**kwargs):
    print(args,kwargs)
    pk = kwargs.get("pk")
    if pk is not None:
      return self.retrieve(request,*args,**kwargs)
    return self.list(request,*args,**kwargs)
  
  def post(self,request,*args,**kwargs):
    return self.create(request,*args,**kwargs)
  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    #print(serializer.validated_data)
    title = serializer.validated_data.get("title")
    content = serializer.validated_data.get("content") or None
    if content is None:
      content = title
    serializer.save(content = content)
    
product_mixim_view = ProductMixinView.as_view()

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