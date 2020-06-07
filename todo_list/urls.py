"""todo_list URL Configuration

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
from django.contrib.auth.views import LogoutView, LoginView

from todo_list_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShowTodoList.as_view(), name='index_page'),
    path('edit_todo/<int:pk>/', edit_todo, name='edit_todo'),
    path('delete_todo/<int:pk>/', delete_todo, name='delete_todo'),
    path('signup/', signup, name='sign_up'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('complete_todo/<int:pk>', complete_todo, name='complete_todo'),
    
]
