from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from expenses.views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('expenses.urls')),
    path('accounts/login/', LoginView.as_view(template_name= 'expenses/login.html'),name='login'),
    path('accounts/logout/',custom_logout,name='logout'),

]
