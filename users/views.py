from math import e
from django.shortcuts import render
from django.contrib.auth import get_user_model
# Импорт служебной формы для регистрации и входа пользователяй
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Импорт редирект
from django.shortcuts import redirect

User = get_user_model()

def register(request):
    context = {
        "form": UserCreationForm(),
        "title": "Регистрация",
        "button_text": "Зарегистрироваться"
    }
    
    if request.method == "POST":
        # Создаем форму регистрации пользователя
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Сохраняем пользователя в базе данных
            form.save()
            # Здесь можно добавить логику для входа пользователя после регистрации
            return redirect('users:login')  # Перенаправляем на страницу входа после успешной регистрации
        
        else:
            # Если форма не валидна, возвращаем ее с ошибками
            context['form'] = form
            return render(request, "users/registr_login.html", context)
        
    else:
        # Если метод запроса GET, создаем пустую форму
        form = UserCreationForm()
        context['form'] = form
    return render(request, "users/registr_login.html", context)

def login(request):
    if request.method == "POST":
        # Здесь будет логика входа пользователя
        pass
    return render(request, "users/login.html")

def logout(request):
    # Здесь будет логика выхода пользователя
    return render(request, "users/logout.html")