from django.urls import path
from dashboard import views
from posts.views import post_create,post_update,post_delete,post_detail,user_post_list,post_list,user_post_detail
from . import views

urlpatterns = [
    path('user/',views.user_dashboard ,name="user_dashboard"),
    path('admin/',views.admin_dashboard, name="admin_dashboard"),
    path('update-activity/', views.update_last_activity, name='update_activity'),
    path('logout/',views.admin_logout ,name="logout"),
    path('authenticator/',views.authenticator,name="authenticator"),
    path('approve/<int:id>/',views.approve_post,name='approve_post'),
    path('reject/<int:id>/',views.reject_post,name='reject_post'),
    path('post_list/',post_list,name='post_list'),
    path('userc/',user_post_list,name='user_post_list'),
    path('create/',post_create,name='post_create'),
    path('update/<int:id>/',post_update,name='post_update'),
    path('delete/<int:id>/',post_delete,name='post_delete'),
    path('detail/<int:id>/',post_detail, name='post_detail'),
    path('user-post-detail/<int:id>/',user_post_detail, name='user_post_detail'),
]