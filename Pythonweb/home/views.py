from django.shortcuts import render
from .forms import RegistrationForm
from .forms import UserUpdateForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.

def get_home(request):
    return render(request,'page1/home.html')
def get_order(request):
    return render(request,'page1/order.html')
def get_guide(request):
    return render(request,'page1/guide.html')
def get_product(request):
    return render(request,'page1/product.html')
def get_contact(request):
    return render(request,'page1/contact.html')
def get_register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') #về trang chủ
    return render(request,'page1/register.html',{'form':form})

def custom_logout(request):
    logout(request)
    return redirect('/') 

def update_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')  # Chuyển hướng sau khi cập nhật
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'page1/profile.html', {'form': form})