"""
URL configuration for bell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 首页
    path('', views.index),

    # 页面
    path('page/<str:pname>', views.page),

    # 归档+文章
    path('archives/', views.archives),
    path('archives/<int:pid>', views.archives),

    # 分类
    path('categories/', views.categories),
    path('categories/<int:cid>', views.categories),

    # 标签
    path('tags/', views.tags),
    path('tags/<int:tid>', views.tags),

    # 搜索
    path('search/', views.search),
]
