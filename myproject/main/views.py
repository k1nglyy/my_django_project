import random
from datetime import datetime
from django.shortcuts import render
from .models import Calculation

def generate_expression():
    num_terms = random.randint(2, 4)
    terms = [random.randint(10, 99) for _ in range(num_terms)]
    operators = [random.choice(['+', '-']) for _ in range(num_terms - 1)]

    expression = str(terms[0])
    for i in range(1, num_terms):
        expression += f" {operators[i-1]} {terms[i]}"

    result = eval(expression)
    return expression, result

def index_page(request):
    context = {
        'course': 'Курс "Промышленное программирование"',
        'author': 'Автор сайта: Полянский Даниил',
        'page_count': 'Количество страниц на сайте: 5',
    }
    return render(request, 'index.html', context)

def time_page(request):
    now = datetime.now()
    context = {
        'course': 'Курс "Промышленное программирование"',
        'date': now.strftime('%d.%m.%Y'),
        'time': now.strftime('%H:%M:%S'),
    }
    return render(request, 'time.html', context)

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

def expression_view(request):
    expression, result = generate_expression()
    Calculation.objects.create(expression=expression, result=result)
    context = {
        'course': 'Курс "Промышленное программирование"',
        'expression': expression,
        'result': result,
    }
    return render(request, 'expression.html', context)

def history_view(request):
    calculations = Calculation.objects.all().order_by('-created_at')
    context = {
        'course': 'Курс "Промышленное программирование"',
        'calculations': calculations,
    }
    return render(request, 'history.html', context)