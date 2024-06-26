from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    logger.info("Index page accessed")
    html = '<a href="about/"> Обо мне </a>  <h1> Главная страница</h1> <p>Домашней работы №1</p>'
    return HttpResponse(html)

def about(request):
    logger.info("About page accessed")
    html = '<h1>Cтраница Обо мне</h1> <p>Я Ларькова Виктория и учусь в GB!</p>'
    return HttpResponse(html)