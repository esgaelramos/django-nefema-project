from django.urls import path

from .views import BlogListView, PostDetailView

app_name='apiblogview'

urlpatterns = [
    path('posts/', BlogListView.as_view(), name='blog-list'),
    path('posts/<post_slug>', PostDetailView.as_view()),
]
