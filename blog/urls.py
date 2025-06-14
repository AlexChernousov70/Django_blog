from django.urls import path
from blog.views import BlogListView, BlogDetailView

app_name = 'blog'

# Псевдонимы будут выглядить так: blog:list и blog:detail
# Все маршруты будут доступну по адресу /blog/
urlpatterns = [
    path("", BlogListView.as_view(), name="post_list"),
    path("<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
]