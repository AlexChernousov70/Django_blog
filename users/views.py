# users/views.py
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import TemplateView


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('landing')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        auth_login(self.request, user)
        messages.success(
            self.request,
            _('Добро пожаловать, %(username)s! Регистрация прошла успешно.') % {
                'username': user.username
            }
        )
        return response
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            _('Пожалуйста, исправьте ошибки в форме регистрации.')
        )
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Регистрация')
        return context

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        messages.success(
            self.request,
            _('С возвращением, %(username)s!') % {
                'username': self.request.user.username
            }
        )
        next_url = self.request.GET.get('next', '')
        return next_url if next_url else super().get_success_url()
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            _('Неверное имя пользователя или пароль. Попробуйте снова.')
        )
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Вход в систему')
        return context

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('landing')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(
                request,
                _('Вы успешно вышли из системы.')
            )
        return super().dispatch(request, *args, **kwargs)

class LandingPageView(TemplateView):
    template_name = "landing.html"
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Дополнительная логика для авторизованных пользователей
            pass
        return super().get(request, *args, **kwargs)