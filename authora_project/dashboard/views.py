from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from account.models import UserRegistration
from posts.models import Posts
from django.contrib import messages
from datetime import timedelta


# USER DASHBOARD
def user_dashboard(request):
    user_id = request.session.get("userId")

    if not user_id:
        return redirect("login")   # change to your login url name

    user = UserRegistration.objects.get(id=user_id)

    return render(request, "user_dashboard.html", {
        "user": user
    })


# ADMIN DASHBOARD
def admin_dashboard(request):
    users = UserRegistration.objects.all()

    online_users = UserRegistration.objects.filter(
        last_activity__gte=timezone.now() - timedelta(minutes=5)
    )

    return render(request, "admin_dashboard.html", {
        "users": users,
        "online_users": online_users
    })


# UPDATE ACTIVITY (called from JS)
def update_last_activity(request):
    user_id = request.session.get("userId")

    if user_id:
        user = UserRegistration.objects.get(id=user_id)
        user.last_activity = timezone.now()
        user.save(update_fields=["last_activity"])

    return JsonResponse({"status": "ok"})

def admin_logout(request):

    request.session.flush()

    return redirect('login')


# AUTHENTICATOR — shows all posts for review
def authenticator(request):
    posts = Posts.objects.all().order_by('-id')
    return render(request, "authenticator.html", {"posts": posts})


# APPROVE POST
def approve_post(request, id):
    post = get_object_or_404(Posts, id=id)
    post.status = 'approved'
    post.save(update_fields=['status'])
    messages.success(request, f'"{post.title}" has been approved!')
    return redirect('authenticator')


# REJECT POST
def reject_post(request, id):
    post = get_object_or_404(Posts, id=id)
    post.status = 'rejected'
    post.save(update_fields=['status'])
    messages.warning(request, f'"{post.title}" has been rejected.')
    return redirect('authenticator')