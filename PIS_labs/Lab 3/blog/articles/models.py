# Импортирую необходимые модули
from django.db import models  # Базовые классы для создания моделей
from django.contrib.auth.models import User  # Модель пользователя Django

# Создаю класс модели Article, наследующий от models.Model
class Article(models.Model):
    # Поле для заголовка статьи
    # CharField - поле для коротких строк
    # max_length=200 - максимальная длина 200 символов
    # Аналог в SQL: VARCHAR(200)
    title = models.CharField(max_length=200)
    
    # Поле для автора статьи - связь с моделью User
    # ForeignKey создает связь "многие к одному"
    # User - модель пользователя, к которой создается связь
    # on_delete=models.CASCADE - при удалении пользователя удаляются его статьи
    # Аналог: можно использовать on_delete=models.SET_NULL для сохранения статей
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Поле для текста статьи
    # TextField - поле для длинного текста без ограничения длины
    # Аналог в SQL: TEXT
    text = models.TextField()
    
    # Поле для даты создания
    # DateField - поле для хранения даты
    # auto_now_add=True - автоматически устанавливает текущую дату при создании
    # Аналог: можно использовать DateTimeField для хранения даты и времени
    created_date = models.DateField(auto_now_add=True)

    # Метод для строкового представления объекта
    # Вызывается при преобразовании объекта в строку
    def __unicode__(self):
        # Возвращаю строку в формате "Имя автора: Заголовок"
        # %s - подстановка строки (старый стиль форматирования)
        # Аналог: можно использовать f"{self.author.username}: {self.title}"
        return "%s: %s" % (self.author.username, self.title)
    
    # Метод для получения краткого отрывка текста
    def get_excerpt(self):
        # Проверяю длину текста
        # Если больше 140 символов - возвращаю первые 140 с многоточием
        # Иначе возвращаю весь текст
        # Тернарный оператор: результат_если_истина if условие else результат_если_ложь
        # Аналог: можно использовать обычный if-else блок
        return self.text[:140] + "..." if len(self.text) > 140 else self.text