from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import BlogModel
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = BlogModel
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = "blog/detail.html"


class BlogUpdateView(UpdateView):
    model = BlogModel
    template_name = "blog/update.html"
    fields = ("title", "memo", "duedate")
    success_url = reverse_lazy('list')


class BlogDeleteView(DeleteView):
    model = BlogModel
    template_name = "blog/delete.html"
    success_url = reverse_lazy('list')
