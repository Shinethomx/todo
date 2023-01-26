"""taskapplication URL Configuration

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
from task.views import AddtastView,TasklistView,TaskDetailView,TaskDeleteView,RegistartionView,LoginnView,signout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',IndexView.as_view()),
    # path('login/',LoginView.as_view()),
    # path('reg/',RegistrationView.as_view()),
    path('todos/add/',AddtastView.as_view(),name="todo-add"),
    path('todos/list/',TasklistView.as_view(),name="todo-list"),
    path('todos/<int:id>',TaskDetailView.as_view(),name="todo-detail"),
    path('todos/delete/<int:id>',TaskDeleteView.as_view(),name="todo-delete"),
    path('account/register/',RegistartionView.as_view(),name="register"),
    path('',LoginnView.as_view(),name="sign-in"),
    path('account/logout/',signout_view,name='sign-out'),

    
]
