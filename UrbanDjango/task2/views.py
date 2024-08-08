from django.shortcuts import render
from django.views.generic import TemplateView

def function_template(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы

    # возвращает функцию render, импортированную по умолчанию в django
    return render(request, 'function_template.html')


class class_template(TemplateView):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы

    template_name = 'class_template.html'
