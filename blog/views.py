from django.views.generic import ListView, DetailView
from .models import BlogModel


class BlogListView(ListView):
    model = BlogModel
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = "blog/detail.html"
