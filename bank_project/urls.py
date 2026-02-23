# bank_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Đảm bảo rằng app users có URL đăng ký, đăng nhập
    path('map/', include('map.urls')),      # Trang bản đồ
    path('accounts/', include('django.contrib.auth.urls')),  # Thêm URL đăng nhập mặc định của Django
    
    # Chuyển hướng trang chủ đến đăng nhập nếu người dùng chưa đăng nhập
    path('', lambda request: redirect('login')),  # Redirect đến trang đăng nhập
]
