from django.urls import path
from dashboard import views
from dashboard import views
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name="register"),
    path('user/',views.user_dashboard ,name="user_dashboard"),
    path('admin/',views.admin_dashboard ,name="admin_dashboard"),
]