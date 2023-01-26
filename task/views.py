import re
from django.shortcuts import redirect, render
from django.urls import is_valid_path


from django.views.generic import View

from task.models import Task 

from django.contrib.auth.models import User


from taskapplication.forms import LoginForm, Registrationform

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages


                                                                                    # Create your views here.

class IndexView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"index.html")


# class LoginView(View):

#     def get(self,request,*args,**kwargs):

#         return render(request,"login.html")


# class RegistrationView(View):

#     def get(self,request,*args,**kwargs):

#         return render(request,"registration.html")

class AddtastView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"Addtask.html")

    def post(self,request,*args,**kwargs):
        user=request.user
        task=request.POST.get("task")
        Task.objects.create(task_name=task,user=user)
        messages.success(request,'task has been created')
        # print(request.POST)
        return render(request,"Addtask.html")


class TasklistView(View):

    def get(self,request,*args,**kw):

        if request.user.is_authenticated:
        # qs=request.user.tasks_set.all()
            qs=Task.objects.filter(user=request.user)

            return render(request,"task-list.html",{"todos":qs})

        else:
            return redirect('sign-in')



class TaskDetailView(View):

    def get(self,request,*args,**kw):

        id=kw.get("id")

        task=Task.objects.get(id=id)

        return render(request,"task-details.html",{"todo":task})

class TaskDeleteView(View):

    def get(self,request,*args,**kw):

        id=kw.get("id")

        Task.objects.filter(id=id).delete()
        messages.success(request,'task deleted')

        return redirect("todo-list")



class RegistartionView(View):

    def get(self,request,*args,**kw):

        form=Registrationform()

    

        return render(request,"register.html",{"form":form})


    def post(self,request,*args,**kw):

        form=Registrationform(request.POST)

        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)

            messages.success(request,'register done !')

            return redirect("todo-list")
        
        else:
            messages.error(request,'registration failed')
            return render(request,"register.html",{"form":form})


class LoginnView(View):

    def get(self,request,*args,**kw):

        form=LoginForm()
        return render(request,"login.html",{'form':form})

    def post(sel,request,*args,**kw):

        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)

            if usr:

               login(request,usr)
               return redirect("todo-list")

            else:

              return render(request,"signin.html",{'form':form})


def signout_view(request,*args,**kw):
    logout(request)
    return redirect('sign-in')




            
