from django.urls import path
from . import views

app_name = 'users'

# Маршруты для приложения users
"""
1. Регистрация пользователя: /register/
2. Вход пользователя: /login/
3. Выход пользователя: /logout/
4. Профиль пользователя: /profile/<int:pk>/
5. Профиль - редактирование: /profile/edit/<int:pk>/
6. Профиль - смена пароля: /profile/change_password/<int:pk>/
7. Восстановление пароля: /password_reset/
"""

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # path("profile/<int:pk>/", name="profile"),
    # path("profile/edit/<int:pk>/", name="edit_profile"),
    # path("profile/change_password/<int:pk>/", name="change_password"),
    # path("password_reset/", name="password_reset"),
]