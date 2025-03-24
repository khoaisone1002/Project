from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import custom_logout
urlpatterns = [
    path('',views.get_home),
    path('order/',views.get_order),
    path('guide/',views.get_guide),
    path('contact/',views.get_contact),
    path('product/',views.get_product),
    path('register/',views.get_register,name='get_register'),
    path('login/', LoginView.as_view(template_name='page1/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    
]