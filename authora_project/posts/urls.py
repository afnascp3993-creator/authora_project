from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('userc/',views.user_post_list,name='user_post_list'),
    path('create/',views.post_create,name='post_create'),
    path('update/<int:id>/',views.post_update,name='post_update'),
    path('delete/<int:id>/',views.post_delete,name='post_delete'),
    path('detail/<int:id>/', views.post_detail, name='post_detail'),
]