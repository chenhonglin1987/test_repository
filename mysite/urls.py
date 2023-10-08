"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from study01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("", views.index),
    # path('user/', views.user_list),
    # path('news/', views.news),
    # path('test/', views.test),
    # path('login/', views.login),
    # path('add/', views.add_user),
    # path('test/', views.test),
    # path('depart/list/', views.depart_list),
    # path('depart/add/', views.depart_add),
    # path('depart/del/', views.depart_del),
    # path('depart/edit/<int:nid>', views.depart_edit),
    # path('class/add/', views.class_add),
    # path('class/list/', views.class_list),
    # path('class/del/', views.class_del),
    # path('class/edit/<int:nid>', views.class_edit),
    # path('user/list/', views.user_list),
    # path('user/add/', views.add_user),

    # ## ManagerSYS路由 ## #
    path('', views.index)
]
