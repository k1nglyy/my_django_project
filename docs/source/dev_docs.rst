Документация разработчика
==========================

Модели
------

Модель Calculation

Модель Calculation предназначена для хранения выражений и их результатов.

Атрибуты:

expression (str): Выражение.
result (float): Результат выражения.
created_at (datetime): Время создания записи.

from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
Модель StringRequest

Модель StringRequest предназначена для хранения запросов строк и их анализа.

Атрибуты:

user (User): Пользователь, отправивший запрос.
input_string (str): Введенная строка.
word_count (int): Количество слов в строке.
char_count (int): Количество символов в строке.
date (date): Дата запроса.
time (time): Время запроса.

from django.db import models
from django.contrib.auth.models import User

class StringRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_string = models.TextField()
    word_count = models.IntegerField()
    char_count = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
Модель Character

Модель Character предназначена для хранения характеристик персонажа.

Атрибуты:

hp (int): Здоровье.
iq (int): Интеллект.
happiness (int): Счастье.

from django.db import models

class Character(models.Model):
    hp = models.IntegerField(default=0)
    iq = models.IntegerField(default=0)
    happiness = models.IntegerField(default=0)

Функции в файле views.py
------------------------

Функция generate_expression

Функция generate_expression генерирует случайное выражение и вычисляет его результат.

Аргументы:

Нет
Возвращает:

tuple: Выражение и его результат.

import random

def generate_expression():
    num_terms = random.randint(2, 4)
    terms = [random.randint(10, 99) for _ in range(num_terms)]
    operators = [random.choice(['+', '-']) for _ in range(num_terms - 1)]

    expression = str(terms[0])
    for i in range(1, num_terms):
        expression += f" {operators[i-1]} {terms[i]}"

    result = eval(expression)
    return expression, result
Функция index_page

Функция index_page отображает главную страницу.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением главной страницы.

from django.shortcuts import render

def index_page(request):
    context = {
        'course': 'Курс "Промышленное программирование"',
        'author': 'Автор сайта: Полянский Даниил',
        'page_count': 'Количество страниц на сайте: 5',
    }
    return render(request, 'index.html', context)
Функция time_page

Функция time_page отображает страницу с текущим временем.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы времени.

from datetime import datetime

def time_page(request):
    now = datetime.now()
    context = {
        'course': 'Курс "Промышленное программирование"',
        'date': now.strftime('%d.%m.%Y'),
        'time': now.strftime('%H:%M:%S'),
    }
    return render(request, 'time.html', context)
Функция calc_page

Функция calc_page отображает страницу калькулятора.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы калькулятора.

def calc_page(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    context = {
        'course': 'Курс "Промышленное программирование"',
        'a': a,
        'b': b,
        'sum': a + b,
    }
    return render(request, 'calc.html', context)
Функция expression_view

Функция expression_view отображает страницу с случайным выражением.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы выражения.

from main.models import Calculation

def expression_view(request):
    expression, result = generate_expression()
    Calculation.objects.create(expression=expression, result=result)
    context = {
        'course': 'Курс "Промышленное программирование"',
        'expression': expression,
        'result': result,
    }
    return render(request, 'expression.html', context)
Функция history_view

Функция history_view отображает страницу истории выражений.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы истории.

def history_view(request):
    calculations = Calculation.objects.all().order_by('-created_at')
    context = {
        'course': 'Курс "Промышленное программирование"',
        'calculations': calculations,
    }
    return render(request, 'history.html', context)
Функция delete_last_expression

Функция delete_last_expression удаляет последнее выражение из истории.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы удаления.

def delete_last_expression(request):
    last_calculation = Calculation.objects.last()
    if last_calculation:
        last_calculation.delete()
    return render(request, 'delete_last_expression.html')
Функция clear_expressions

Функция clear_expressions очищает все выражения из истории.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы очистки.

def clear_expressions(request):
    Calculation.objects.all().delete()
    return render(request, 'clear_expressions.html')
Функция add_new_expression

Функция add_new_expression добавляет новое выражение.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы добавления выражения.

def add_new_expression(request):
    expression_text = request.GET.get('expression')
    if expression_text:
        try:
            result = eval(expression_text)
            Calculation.objects.create(expression=expression_text, result=result)
            return render(request, 'add_new_expression.html', {'message': 'Ваше выражение добавлено'})
        except Exception as e:
            return render(request, 'add_new_expression.html', {'message': f'Ошибка при вычислении выражения: {e}'})
    else:
        return render(request, 'add_new_expression.html', {'message': 'Для добавления нового выражения используйте URL-параметр expression. Пример: /new/?expression=ваше_выражение'})
Функция str2words

Функция str2words отображает страницу подсчета слов в строке.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы подсчета слов.

from django.contrib.auth.decorators import login_required
import re

@login_required
def str2words(request):
    if request.method == 'POST':
        input_string = request.POST.get('input_string', '')
        words = re.findall(r'\b\w+\b', input_string)
        numbers = re.findall(r'\b\d+\b', input_string)

        word_count = len(words)
        number_count = len(numbers)

        StringRequest.objects.create(
            user=request.user,
            input_string=input_string,
            word_count=word_count,
            char_count=len(input_string.replace(' ', '')),
            date=datetime.now().date(),
            time=datetime.now().time()
        )

        context = {
            'input_string': input_string,
            'word_count': word_count,
            'number_count': number_count,
            'words': words,
            'numbers': numbers,
        }
        return render(request, 'str2words.html', context)
    return render(request, 'str2words.html')
Функция str_history

Функция str_history отображает страницу истории строк.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы истории строк.

@login_required
def str_history(request):
    history = StringRequest.objects.filter(user=request.user).order_by('-date', '-time')
    context = {
        'history': history,
    }
    return render(request, 'str_history.html', context)
Функция clicker_view

Функция clicker_view отображает страницу кликера.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

HttpResponse: Ответ с отображением страницы кликера.

from main.forms import CharacterForm

def clicker_view(request):
    character, created = Character.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return JsonResponse({'hp': character.hp, 'iq': character.iq, 'happiness': character.happiness})
    else:
        form = CharacterForm(instance=character)
    return render(request, 'clicker.html', {'form': form, 'character': character})
Функция update_parameter

Функция update_parameter обновляет параметры персонажа.

Аргументы:

request (HttpRequest): Объект запроса.
Возвращает:

JsonResponse: Ответ с обновленными параметрами персонажа.

from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update_parameter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        character, created = Character.objects.get_or_create(id=1)
        character.hp = data.get('hp', character.hp)
        character.iq = data.get('iq', character.iq)
        character.happiness = data.get('happiness', character.happiness)
        character.save()
        return JsonResponse({'hp': character.hp, 'iq': character.iq, 'happiness': character.happiness})
    return JsonResponse({'error': 'Invalid request method'}, status=400)