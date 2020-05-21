from django.views.generic import ListView
from .models import BlogModel


class BlogListView(ListView):
    model = BlogModel
    template_name = "blog/home.html"
