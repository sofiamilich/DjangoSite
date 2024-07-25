
from django.shortcuts import render
from django.views.generic import TemplateView

def third_task(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы


    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'



    context = {
        'link1':link1,
        'link2':link2,
        'link3':link3,
    }
    # возвращает функцию render, импортированную по умолчанию в django
    return render(request, 'third_task.html', context)


def index(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы

    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']

    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
        'list': list,
    }

    # возвращает функцию render, импортированную по умолчанию в django
    return render(request, 'index.html', context)

def index1(request):

    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'


    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    # Напишем переменную, передающую имя второй страницы:
    return render(request, 'index1.html', context)

def menu(request):
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']

    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
        'list': list,
    }
    # Напишем переменную, передающую имя второй страницы:
    return render(request, 'menu.html', context)

