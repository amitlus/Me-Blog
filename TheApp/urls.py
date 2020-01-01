from . import views
from django.urls import path

# template URLs
app_name = 'TheApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('<str:user.username>/', views.userblog, name='userblog'),
    path('draft', views.draft, name='draft'),
    path('explore', views.Explore.as_view(), name='explore'),#נטו בשביל הtemplate url בbase כדי שבלחיצה על האקספלור בסרגל זה יעביר אותי

]
