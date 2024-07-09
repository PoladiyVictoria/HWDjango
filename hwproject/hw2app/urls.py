from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:client_id>', views.orders, name='orders_client'),
    path('prod_add/', views.product_action, name='prod_add'),
    path('find_prod/', views.get_product, name='find_prod'),
]