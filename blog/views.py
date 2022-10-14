from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class BlogListView(ListView):
          """Blog List View """

          model = Post
          template_name = "home.html"


class BlogDetailView(DetailView):
          """Blog detail """
          model = Post
          template_name ="post_detail.html"

class BlogCreateView(LoginRequiredMixin, CreateView):
          """ Blog Create View """
          model = Post
          template_name = "post_new.html"
          fields = ["title", "author", "body"]
          # success_url = "home " you can redirect to a destination of a url

class BlogUpdateView(LoginRequiredMixin, UpdateView):
           """ Blog Udate View """

           model = Post
           template_name = "post_edit.html"
           fields = ["title", "body"]

class BlogDeleteView(LoginRequiredMixin, DeleteView):
          """ Blog Delete View"""
          model = Post
          template_name = "post_delete.html"
          success_url = reverse_lazy("home")