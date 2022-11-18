from django.urls import path

from . import views

urlpatterns = [
  # path("",views.ProductCreateAPIVIiew.as_view()),
  path("<int:pk>/",views.product_alt_view),
  path("",views.product_alt_view),
  
]