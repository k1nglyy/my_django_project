from django.shortcuts import render
from datetime import datetime

def index_page(request):
    context = {
        'course': 'Курс "Промышленное программирование"',
        'author': 'Автор сайта: Полянский Даниил',
        'page_count': 'Количество страниц на сайте: 3',
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