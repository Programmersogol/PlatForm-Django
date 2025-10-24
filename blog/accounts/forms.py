from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "مثلاً: zynab_king"}),
        help_text="", 
    )

    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "ایمیل خود را وارد کنید"}),
        help_text="",
    )

    bio = forms.CharField(
        label="درباره من",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "چند خط درباره‌ی خودت بنویس..."}),
        required=False,
    )

    avatar = forms.ImageField(
        label="آواتار",
        widget=forms.FileInput(attrs={"class": "form-control"}),
        required=False,
    )

    password1 = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور خود را وارد کنید"}),
    )
    password2 = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور را دوباره وارد کنید"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "bio", "avatar"]


class ProfileForm(forms.ModelForm):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "مثلاً: zynab_king"}),
        help_text="",  
    )

    class Meta:
        model = User
        fields = ['username', 'bio', 'avatar']
        labels = {
            'bio': 'بیوگرافی',
            'avatar': 'عکس پروفایل',
        }
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'چند خط درباره‌ی خودت بنویس...',
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
