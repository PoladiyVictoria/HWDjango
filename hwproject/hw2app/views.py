from datetime import datetime, timedelta
import logging
from django.shortcuts import get_object_or_404, render
from .models import Order,Client, Product
from .forms import Product_form, Get_Product
from django.core.files.storage import FileSystemStorage

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


def product_action(request):
    if request.method == 'POST':
        form = Product_form(request.POST, request.FILES)
        if form.is_valid():
            res = form.cleaned_data
            fs = FileSystemStorage()
            fs.save(res['image'].name, res['image'])
            product = Product(
                name = res['name'],
                description = res['description'],
                price = res['price'],
                quantity = res['quantity'],
                path_to_image = '../../../media/' + res['image'].name
            )
            product.save()
            logger.info(f'Product {res["name"]} added')
    else:
        form = Product_form()
    return render(request, 'hw2app/product_form.html', {'form': form})


def get_product(request):
    if request.method == "POST":
        form = Get_Product(request.POST)
        if form.is_valid():
            prod = form.cleaned_data['name']
            some_prod = Product.objects.filter(name = prod).first()
            return render(request, 'hw2app/get_product.html', {'some_prod': some_prod})
    else:
        form = Get_Product()
    return render(request, 'hw2app/get_product_form.html', {'form': form})