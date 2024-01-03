from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password_repeat = forms.CharField(max_length=100, widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100, required=False)

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise forms.ValidationError('Опа, стоять, пароли то разные.')

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Чувачок с такой же почтой уже есть, нук попробуй ещё раз.')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError('Слишком короткий...пароль, надо длиннее')

        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Неа, такое имя пользователя уже есть, будь оригинальнее')

        return username


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Нет такого, а ну-ка, или проверь или регистрируйся')

        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = User.objects.get(username=username)

        if not user.check_password(password):
            raise forms.ValidationError('Нет такого, а ну-ка, или проверь или регистрируйся')

        return password
