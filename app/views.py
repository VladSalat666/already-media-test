from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, 'index.html')


def handle_form(request):
  if request.method == 'POST':
    # Обработка данных формы
    data = request.POST
    # Выполнение логики обработки данных
    return HttpResponse("Форма обработана")
  else:
    return HttpResponse("Метод не поддерживается")
