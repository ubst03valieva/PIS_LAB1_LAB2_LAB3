# Импортирую модель Article из текущего приложения
from .models import Article
# Импортирую функцию render для отображения шаблонов
from django.shortcuts import render

# Создаю функцию представления archive
# request - объект HTTP-запроса от клиента
def archive(request):
    # Использую функцию render для отображения шаблона
    # Первый параметр - объект запроса
    # Второй параметр - путь к шаблону
    # Третий параметр - словарь контекста с данными для шаблона
    # Article.objects.all() - получаю все статьи из базы данных
    # Аналог: можно использовать Article.objects.filter(author=request.user)
    return render(request, 'archive.html', {"posts": Article.objects.all()})