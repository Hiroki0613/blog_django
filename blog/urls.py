from django.urls import path
from .views import BlogListView, BlogDetailView, BlogUpdateView

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update'),
]
