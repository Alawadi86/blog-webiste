from django.views.generic import ListView

# Create your views here.

from .models import Post

class BlogListView(ListView):
          """Blog List View """

          model = Post
          template_name = "home.html"

          

