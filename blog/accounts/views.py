from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import SignUpForm,ProfileForm  # فرم جدید رو وارد کن
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from page.models import Post 
User = get_user_model()

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)  
        if form.is_valid():
            user = form.save()  
            login(request, user)
            messages.success(request, "ثبت‌نام با موفقیت انجام شد ✅")
            return redirect("post_list")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "خوش اومدی 🌸")
            return redirect("post_list")
        else:
            messages.error(request, "نام کاربری یا رمز اشتباهه")
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "خروج با موفقیت انجام شد 👋")
    return redirect("post_list")




class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "profile_form.html"
    success_url = reverse_lazy("post_list")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "پروفایل با موفقیت به‌روزرسانی شد! ✅")
        return response
    


def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-created_at')
    return render(request, 'profile_detail.html', {
        'profile_user': user,
        'posts': posts
    })
