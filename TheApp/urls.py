from . import views
from django.urls import path

# template URLs
app_name = 'TheApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('userblog', views.blog_name, name='userblog'),
    path('draft', views.draft, name='draft'),
]
