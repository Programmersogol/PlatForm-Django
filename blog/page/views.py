# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from comments.models import Comment
from django.utils.text import slugify
from django.db.models import Q


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  
    template_name = "page/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.title, allow_unicode=True)
            num = 1
            base_slug = form.instance.slug
            while Post.objects.filter(slug=form.instance.slug).exists():
                form.instance.slug = f"{base_slug}-{num}"
                num += 1
        response = super().form_valid(form)
        messages.success(self.request, "پست با موفقیت ایجاد شد! ✅")
        return response

    def get_success_url(self):
        if not self.object.slug:
            messages.warning(self.request, "اسلاگ تولید نشد، به لیست پست‌ها هدایت شدید.")
            return reverse("post_list")
        return reverse("post_detail", kwargs={"slug": self.object.slug})

class PostListView(ListView):
    model=Post
    template_name="page/post_list.html"
    context_object_name="posts"
    paginate_by=5
    ordering=["-created_at"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        posts = Post.objects.all().order_by("-created_at")
        if query:
            posts = posts.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(category__name__icontains=query) |
                Q(author__username__icontains=query) |   
                Q(author__bio__icontains=query)         
            )
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class PostDetailView(DetailView): 
    model = Post
    template_name = "page/post_detail.html"
    context_object_name = "post"


class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "page/post_form.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff
 
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "پست با موفقیت حذف شد ✅")
        return super().delete(request, *args, **kwargs)



@login_required
def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.info(request, "لایک حذف شد 👎")
    else:
        post.likes.add(request.user)
        messages.success(request, "پست لایک شد ❤️")
    return HttpResponseRedirect(reverse('post_list'))



@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Comment.objects.create(post=post, user=request.user, text=text)

    return redirect("post_list") 