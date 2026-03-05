from django.shortcuts import render,redirect,get_object_or_404
from .models import Category
from .forms import CategoryForm


# READ
def category_list(request):
    categories = Category.objects.all()
    return render(request,'categories/category_list.html',{'categories':categories})


# CREATE
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request,'categories/category_form.html',{'form':form})


# UPDATE
def category_update(request,id):
    category = get_object_or_404(Category,id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request,'categories/category_form.html',{'form':form})


# DELETE
def category_delete(request,id):
    category = get_object_or_404(Category,id=id)
    if request.method == "POST":
        category.delete()
        return redirect('category_list')
    return render(request,'categories/category_delete.html',{'category':category})