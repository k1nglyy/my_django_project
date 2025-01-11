from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StringRequest, Calculation
import re
import random
from datetime import datetime

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

def delete_last_expression(request):
    last_calculation = Calculation.objects.last()
    if last_calculation:
        last_calculation.delete()
    return render(request, 'delete_last_expression.html')

def clear_expressions(request):
    Calculation.objects.all().delete()
    return render(request, 'clear_expressions.html')

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

@login_required
def str_history(request):
    history = StringRequest.objects.filter(user=request.user).order_by('-date', '-time')
    context = {
        'history': history,
    }
    return render(request, 'str_history.html', context)