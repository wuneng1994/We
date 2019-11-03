"""We URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('index/all/<int:type_id>.html', views.index,name='index'),
    path('register.html',views.Register.as_view(),name='register'),
    path('login.html',views.Login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('apply_verify_code',views.apply_verify_code,name='apply_verify_code'),
	path('<str:blog>.html/',views.blog,name = "blog"),
	path('<str:blog>/<str:article_id>.html/',views.get_article,name = "get_article")

]
