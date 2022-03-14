from django.urls import path

from anews import views

app_name='anews'

urlpatterns = [
    path('news', views.render_posts, name='posts'),
    path('news/<int:post_id>', views.post_detail, name='post_detail'),
]