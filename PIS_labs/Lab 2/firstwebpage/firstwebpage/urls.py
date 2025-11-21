"""
URL configuration for firstwebpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Импортирую необходимые модули
from django.contrib import admin  # Модуль административной панели
from django.urls import path       # Функция для определения путей
from flatpages import views        # Импортирую views из приложения flatpages

# Определяю список URL-паттернов проекта
urlpatterns = [
    # Маршрут для административной панели
    # admin.site.urls содержит все URL админки
    path('admin/', admin.site.urls),
        # Главная страница - вызывает функцию home из views
    # name='home' - именованный URL для использования в шаблонах
    path('', views.home, name='home'),

    # Добавляю новый маршрут для адреса /hello/
    # Использую ту же функцию home для обработки
    path('hello/', views.home, name='hello'),

]