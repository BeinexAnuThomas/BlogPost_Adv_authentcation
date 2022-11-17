from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm,CreateUserForm,LoginForm,CreateBlogForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DeleteView,CreateView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, "index.html")
    


def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are registered Successfully !!!")
            return redirect('login')
    context={'form':form}
    return render(request,"register.html",context=context)

class Register(CreateView):
    def dispatch(self, request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request,*args,**kwargs)
    template_name = "register.html"
    form_class = CreateUserForm
    success_url = reverse_lazy('home')

def login(request):
    form=LoginForm
    if request.method=='POST':
        form= LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, "You are logged in Successfully !!!")
                return redirect('dashboard')
            
    context={'form':form}
    return render(request,"login.html",context=context)



def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out Successfully !!!")
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    return render(request,"dashboard.html")


@login_required(login_url='login')
def createBlog(request):
    form=CreateBlogForm(request.POST,request.FILES)
    blog=Blog.objects.all()
    
    if request.method =='POST':
        form=CreateBlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=request.user
            form.save()
            messages.success(request, "New blog created Successfully !!!")
            return redirect('viewBlog')

    context={'form':form}
    return render(request, 'createBlog.html',context=context)


@login_required(login_url='login')
def viewBlog(request): 
    # current_user = request.user.id
    # blog=Blog.objects.all().filter(user=current_user)   
    blog=Blog.objects.all()
    context={'blog':blog}
    return render(request, 'viewBlog.html',context=context)


@login_required(login_url='login')
def updateBlog(request,pk):
    blog=Blog.objects.get(id=pk)
    form= CreateBlogForm(request.POST or None,instance=blog)
    if request.method=='POST':
        form= CreateBlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated Successfully !!!")
            return redirect('viewBlog')
    context={'form':form}
    return render(request, 'updateBlog.html',context=context)


@login_required(login_url='login')
def deleteBlog(request,pk):
    blog=Blog.objects.get(id=pk)   
    if request.method=='POST':
        blog.delete()
        messages.success(request, "Task Deleted Successfully !!!")
        return redirect('viewBlog')
    
    context={'object':blog}
    return render(request, 'deleteBlog.html',context=context)
