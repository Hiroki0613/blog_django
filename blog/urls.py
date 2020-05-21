from django.urls import path
from .views import Home, BlogListView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('list/', BlogListView.as_view(), name='list')
]
