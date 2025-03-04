# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Если у вас своя модель пользователя (где есть role, about, photo),
# импортируйте её. Например:
# from .models import User

def login_view(request):
    """
    Отображает страницу логина. При POST проверяет username/password,
    если верны — логинит и перенаправляет на profile.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password!')
    # Если GET или неуспешная аутентификация, рендерим шаблон логина
    return render(request, 'accounts/login.html')


def register_view(request):
    """
    Отображает страницу регистрации (UserCreationForm).
    При POST, если форма валидна, создаёт нового пользователя.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    """
    Выход пользователя (logout), после чего перенаправляем на login.
    """
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    """
    Пример страницы профиля. Требует, чтобы пользователь был залогинен.
    """
    return render(request, 'accounts/profile.html')


@login_required
def profile_edit_view(request):
    """
    Пример редактирования профиля. Мы предполагаем, что ваша модель пользователя
    имеет поля: username, role, about, photo.
    При POST сохраняем новые данные и переходим на profile.
    """
    user = request.user
    if request.method == 'POST':
        # Обновляем поля напрямую (самый простой способ).
        # Убедитесь, что в вашей модели User действительно есть поля 'role', 'about', 'photo'.
        user.username = request.POST.get('username', user.username)
        user.role = request.POST.get('role', getattr(user, 'role', ''))
        user.about = request.POST.get('about', getattr(user, 'about', ''))
        if 'photo' in request.FILES:
            user.photo = request.FILES['photo']

        user.save()
        messages.success(request, 'Профиль обновлён!')
        return redirect('profile')

    # Если GET — показываем страницу с текущими значениями
    return render(request, 'accounts/profile_edit.html', {'user': user})
