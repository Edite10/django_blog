from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


def my_blog(request):
    return HttpResponse("Welcome to my blog")


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Post.objects.filter(status=1)  # Only published posts
        
        # Handle filtering and sorting
        sort_by = self.request.GET.get('sort', '-created_on')
        search_query = self.request.GET.get('q', '')
        
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query)
            )
        
        # Apply sorting
        if sort_by == 'likes':
            # This is a bit trickier with annotation, but simplified for now
            return sorted(queryset, key=lambda p: p.total_likes(), reverse=True)
        elif sort_by == 'loves':
            return sorted(queryset, key=lambda p: p.total_loves(), reverse=True)
        else:
            return queryset.order_by(sort_by)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort'] = self.request.GET.get('sort', '-created_on')
        context['search_query'] = self.request.GET.get('q', '')
        return context


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Post.objects.filter(author=self.request.user)
        
        # Handle filtering and sorting
        sort_by = self.request.GET.get('sort', '-created_on')
        search_query = self.request.GET.get('q', '')
        
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query)
            )
        
        return queryset.order_by(sort_by)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort'] = self.request.GET.get('sort', '-created_on')
        context['search_query'] = self.request.GET.get('q', '')
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        # Check if user has liked or loved
        if self.request.user.is_authenticated:
            context['liked'] = post.likes.filter(id=self.request.user.id).exists()
            context['loved'] = post.loves.filter(id=self.request.user.id).exists()
        
        # Add comment form
        context['comment_form'] = CommentForm()
        context['comments'] = post.comments.filter(active=True)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('my_posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your post has been created!')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your post has been updated!')
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('my_posts')
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


@login_required
def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
            
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'liked': liked,
                'total_likes': post.total_likes()
            })
            
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def post_love(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        if post.loves.filter(id=request.user.id).exists():
            post.loves.remove(request.user)
            loved = False
        else:
            post.loves.add(request.user)
            loved = True
            
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'loved': loved,
                'total_loves': post.total_loves()
            })
            
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added.')
            
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
