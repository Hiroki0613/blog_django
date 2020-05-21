from django.views.generic import TemplateView, ListView
from .models import BlogModel


class Home(TemplateView):
    template_name = 'blog/home.html'


class BlogListView(ListView):
    model = BlogModel
    template_name = "list.html"
