from datetime import datetime, timedelta
import logging
from django.shortcuts import get_object_or_404, render
from .models import Order,Client

logger = logging.getLogger(__name__)

def index(request):
    logger.info("Index page accessed")
    context = {
        'title': 'Главная страница',
        'content': 'Перейдите по ссылке'
    } 
    return render(request, "hw2app/index.html", context)

def orders(request, client_id: int = None):
    logger.info("Orders page accessed")
    if client_id:
        client = get_object_or_404(Client, id=client_id)
        order = Order.objects.filter(client=client)
        today = datetime.now()
        
        order_week = order.filter(order_date__gte=today-timedelta(days=7))
        order_month = order.filter(order_date__gte=today-timedelta(days=30))
        order_year = order.filter(order_date__gte=today-timedelta(days=365))
        
        products_week = {product for order in order_week for product in order.order.all()}
        products_month = {product for order in order_month for product in order.order.all()}
        products_year = {product for order in order_year for product in order.order.all()}
        
        context = {
            "title": f"Список заказов клиента {client.name}",
            "client": client,
            "order": order,
            "products_week": products_week,
            "products_month": products_month,
            "products_year": products_year,
        }
    else:
        order = Order.objects.all()
        context = {"title": f"Список всех заказов", "order": order}
    return render(request, "hw2app/order.html", context)