import logging
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)

def index(request):
    logger.info("Index page accessed")
    html = '<h1> Главная страница</h1> <p>Домашней работы №2</p>'
    return HttpResponse(html)
