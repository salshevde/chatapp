from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login ,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("chat:chat")
    else:
        form = UserCreationForm()
    return render(request,'register.html',{"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("chat:chat")
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{"form": form})

@login_required(login_url="/users/login")
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:login")

@login_required(login_url="/users/login")
def profile(request):
    user = request.user
    return render(request,'profile.html',{'user':user})
