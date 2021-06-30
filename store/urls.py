from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='Home'),
  path('store/', views.store, name='Products'),
  path('about/', views.about, name='About'),
  path('contact/', views.contact, name='Contact'),
  path('tracker/', views.tracker, name='Status'),
  path('store/search/', views.search, name='Search'),
  path('productInfo/<int:id>', views.productInfo, name='Info'),
  path('checkout/', views.checkout, name='Checkout'),
]
