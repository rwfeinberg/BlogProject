# Contains both function-based and class-based views in Django

from typing import List
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User

# Class-based: Defines home page located at '/'. 
class PostListView(ListView):
    model = Post                                            # active model
    template_name = 'blog/home.html'                        # HTML template for page
    context_object_name = 'posts'                           # name of 'object' within template
    ordering = ['-date_posted']                             # how to order posts on homepage
    paginate_by = 5                                         # objects per page

# Class-based: Defines home page located at '/user/USERNAME'. 
class UserPostListView(ListView):
    model = Post                                            # active model
    template_name = 'blog/user_posts.html'                  # HTML template for page
    context_object_name = 'posts'                           # name of 'object' within template                            # how to order posts on homepage
    paginate_by = 5                                         # objects per page

    def get_queryset(self):                                 # overridden method to get posts from user
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# Class-based: Defines post page located at '/post/#/'
class PostDetailView(DetailView):
    model = Post

# Class-based: Defines post delete page located at '/post/#/delete'
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'                                       # URL to be redirected to when post is deleted

    def test_func(self):                                    # overridden function to check that post author matches current logged in user when deleting
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Class-based: Defines post creation page located at '/post/new/'
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']                           # Fields to appear on page

    def form_valid(self, form):                             # overriden function to set post author as current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

# Class-based: Defines post update page located at '/post/#/update/'
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']                           # Fields to appear on page

    def form_valid(self, form):                             # overriden function to set post updater as current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):                                    # overriden function to check that post author matches current lgogged in user when updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Function-based: Defines about page located at '/about/'
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # Uses about.html as template; Context is only the 'About' title

# Function-based: Defines special page located at '/special/'
def special(request):
    return render(request, 'blog/special.html')             # Uses special.html as template

