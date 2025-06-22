from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Имя пользователя или email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Пароль'
        })

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-2', 
            'placeholder': 'Email'
        }),
        required=True,
        help_text="Обязательное поле.",
        label="Электронная почта"
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Имя пользователя',
            'minlength': '4'
        })
        self.fields['username'].help_text = "Только буквы, цифры и @/./+/-/_."
        self.fields['username'].label = "Логин"
        
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mb-2',
            'placeholder': 'Придумайте пароль',
            'minlength': '8'
        })
        self.fields['password1'].label = "Пароль"
        
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Повторите пароль',
            'minlength': '8'
        })
        self.fields['password2'].label = "Подтверждение пароля"
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже существует.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user