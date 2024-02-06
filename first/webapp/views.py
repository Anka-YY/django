from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Registration, Category, TodoList
from django.http import HttpResponse
from datetime import datetime


# Открывается главная страница
def index(request):
    data = {'content': 'Для работы приложения необходимо авторизоваться'}
    return render(request, 'index.html', context=data)


# Открывается страница регистрации
def registration(request):
    return render(request, 'registration.html')


# Открывается страница авторизвации
def authorization(request):
    return render(request, 'authorization.html')


# Функция регистрации
def sendDataRegistration(request):
    tempData = request.POST.dict()
    login = tempData.get('login')
    password = tempData.get('password')
    email = tempData.get('email')

    if bool(login) and bool(password) and bool(email):
        try:
            Registration.objects.get(login=login)
        except ObjectDoesNotExist:
            Registration.objects.create(login=login, password=password, email=email)
            data = {'message': 'Регистрация завершена'}
            return render(request, 'registration.html', context=data)
        else:
            data = {'message': 'Такой логин уже занят'}
            return render(request, 'registration.html', context=data)
    else:
        data = {'message': 'Введите корректные данные'}
        return render(request, 'registration.html', context=data)


# Функция авторизации
def getDataAuthorization(request):
    tempData = request.POST.dict()
    login = tempData.get('login')
    password = tempData.get('password')

    if bool(login) and bool(password):
        try:
            tempUser = Registration.objects.get(login=login)
        except ObjectDoesNotExist:
            data = {'message': 'Пользователь не найден'}
            return render(request, 'authorization.html', context=data)
        else:
            if tempUser.password == password:
                data = {'message': 'Привет, ' + login}
                return redirect('/todo', context=data)
            else:
                data = {'message': 'Не верный пользователь или пароль'}
                return render(request, 'authorization.html', context=data)
    else:
        data = {'message': 'Введите корректные данные'}
        return render(request, 'authorization.html', context=data)



def todo(request):
    todos = TodoList.objects.filter(due_date='2000-01-01 00:00:00')
    print(todos)
    todo_done = TodoList.objects.exclude(due_date='2000-01-01 00:00:00')
    print(todo_done)
    categories = Category.objects.all()
    return render(request, 'todo.html', {'todos': todos, 'categories': categories, 'todo_done': todo_done})


def todoAdd(request):
    if request.method == 'POST':
        title = request.POST['description']
        date = datetime.today()
        category = request.POST['category_select']
        category_id = Category.objects.get(name=category)
        content = request.POST['content']
        TodoList.objects.create(title=title, content=content, due_date='2000-01-01 00:00:00', category_id=category_id.id, created = date)
        return redirect('/todo')


def todoDelete(request):
    if request.method == 'POST':
        checkedlist = request.POST.getlist('checkedbox')
        for i in range(len(checkedlist)):
            todo = TodoList.objects.filter(id=int(checkedlist[i]))
            todo.delete()
    return redirect('/todo')


def todoDone(request):
    if request.method == 'POST':
        checkedlist = request.POST.getlist('checkedbox')
        for i in range(len(checkedlist)):
            date = datetime.today()
            todo = TodoList.objects.filter(id=int(checkedlist[i])).update(due_date=date)
    return redirect('/todo')


def category(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        if 'Add' in request.POST:
            name = request.POST['name']
            category = Category(name=name)
            category.save()
            return redirect('/category')
    if 'Delete' in request.POST:
        check = request.POST.getlist('check')
        for i in range(len(check)):
            try:
                categ = Category.objects.filter(id=int(check[i]))
                categ.delete()
            except BaseException:
                return HttpResponse('<h1>Сначала удалите карточки с этими категориями<h1>')
    return render(request, 'category.html', {'categories':categories})


