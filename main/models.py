from django.db import models
from django.contrib.auth.models import User

class Calculation(models.Model):
    """
    Модель для хранения выражений и их результатов.

    Атрибуты:
        expression (str): Выражение.
        result (float): Результат выражения.
        created_at (datetime): Время создания записи.
    """
    expression = models.CharField(max_length=255)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class StringRequest(models.Model):
    """
    Модель для хранения запросов строк и их анализа.

    Атрибуты:
        user (User): Пользователь, отправивший запрос.
        input_string (str): Введенная строка.
        word_count (int): Количество слов в строке.
        char_count (int): Количество символов в строке.
        date (date): Дата запроса.
        time (time): Время запроса.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_string = models.TextField()
    word_count = models.IntegerField()
    char_count = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

class Character(models.Model):
    """
    Модель для хранения характеристик персонажа.

    Атрибуты:
        hp (int): Здоровье.
        iq (int): Интеллект.
        happiness (int): Счастье.
    """
    hp = models.IntegerField(default=0)
    iq = models.IntegerField(default=0)
    happiness = models.IntegerField(default=0)