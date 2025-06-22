from django.contrib import admin
from django.urls import path
from blog import urls as blog_urls
from users import urls as users_urls
from users.views import LandingPageView
from django.views.generic import TemplateView
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog_urls, namespace='blog') ),
    path('users/', include(users_urls, namespace='users')),
    path('', LandingPageView.as_view(), name='landing'),
]