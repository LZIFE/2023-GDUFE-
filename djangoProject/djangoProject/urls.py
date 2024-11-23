"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#
# from django.contrib import admin
from django.urls import path
from app01 import views
from app01 import upload

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('signup/', views.index),

    path('scholarship/', views.scholarship, name='scholarship'),
    path('teacher_evaluation/', views.teacher_evaluation, name='teacher_evaluation'),
    path('mainmenu/', views.main_menu),
    path('submitproject/', views.submitproject, name='submitproject'),
    path('upload/', upload.upload, name='upload_file',),


]
