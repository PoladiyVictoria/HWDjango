from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:client_id>', views.orders, name='orders_client'),
]