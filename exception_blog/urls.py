from django.contrib import admin
from django.urls import path
from blog import urls as blog_urls
from users import urls as users_urls
# Импорт икнлюда
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog_urls, namespace='blog') ),
    path('users/', include(users_urls, namespace='users')),
]