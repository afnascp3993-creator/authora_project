from django.urls import path
from . import views

urlpatterns = [
path('',views.category_list,name='category_list'),
path('create/',views.category_create,name='category_create'),
path('update/<int:id>/',views.category_update,name='category_update'),
path('delete/<int:id>/',views.category_delete,name='category_delete'),
]   