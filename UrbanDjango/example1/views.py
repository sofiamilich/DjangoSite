from django.shortcuts import render
from django.views.generic import TemplateView
#def third_task(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы

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
    #return render(request, 'fourth_task/third_task.html', context)

# Создадим вторую страницу при помощи класса наследуемого:
class index(TemplateView):
    # Напишем переменную, передающую имя второй страницы:
    template_name = 'index.html'

class index1(TemplateView):
    # Напишем переменную, передающую имя второй страницы:
    template_name = 'index1.html'
