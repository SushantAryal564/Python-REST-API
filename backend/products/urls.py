from django.urls import path

from . import views

urlpatterns = [
  # path("",views.ProductCreateAPIVIiew.as_view()),
  path("<int:pk>/update",views.product_update_view),
  path("<int:pk>/delete",views.product_delete_view),
  path("<int:pk>/",views.product_mixim_view),
  path("",views.product_mixim_view),
  
]