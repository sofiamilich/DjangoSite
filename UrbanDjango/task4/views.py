
from django.shortcuts import render
from django.views.generic import TemplateView

def third_task(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы

    title = 'имя сайта'
    h1 = 'Главная страница'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    context = {
        'title':title,
        'h1' : h1,
        'link1':link1,
        'link2':link2,
        'link3':link3,
    }
    # возвращает функцию render, импортированную по умолчанию в django
    return render(request, 'third_task.html', context)


def index(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы

    list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    h1 = 'text_h1'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'


    context = {
        'h1':h1,
        'link1' : link1,
        'link2': link2,
        'link3': link3,
        'list': list,
    }

    #first = 'Atomic Heart'
    #second = 'Cyberpunk 2077'
    #third = 'PayDay 2'

    #context = {
        #'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    #}
        #'first':first,
        #'second' : second,
        #'third': third,

    # возвращает функцию render, импортированную по умолчанию в django
    return render(request, 'index.html', context)


# Создадим вторую страницу при помощи класса наследуемого:
#class index(TemplateView):
    # Напишем переменную, передающую имя второй страницы:
   # template_name = 'index.html'

class index1(TemplateView):
    # Напишем переменную, передающую имя второй страницы:
    template_name = 'index1.html'


class menu(TemplateView):
    # Напишем переменную, передающую имя второй страницы:
    template_name = 'menu.html'