# Импортирую дополнительные модули для работы с шаблонами
from django.shortcuts import render  # Функция для рендеринга шаблонов
from django import template          # Модуль шаблонов Django

def home(request):
    # Использую функцию render для отображения шаблона
    # request - объект запроса, передается в шаблон
    # 'templates/index.html' - путь к файлу шаблона
    # render автоматически загружает шаблон и возвращает HttpResponse с HTML
    # Аналог: можно использовать loader.get_template() и template.render()
    return render(request, 'templates/static_handler.html')