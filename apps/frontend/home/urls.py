from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('symptom/', views.symptom, name='symptom'),
    path('mail-us/', views.mailus, name='mail_us'),
    # path('product-data/', views.GetProductList.as_view(), name='product_list'),
]
