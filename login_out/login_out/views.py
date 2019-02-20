from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request,'login.html')

@login_required(login_url="in")
def welcome(request):
    return HttpResponse("YOU ARE LOGED IN")

# def f(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("chbhf")
#     return render(request,'form.html')

def Login(request):
        if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)
                if form.is_valid():
                        user = form.get_user()
                        login(request ,user)
                        if request.POST['username'] == "rishav":
                                return redirect("welc")
                        else:
                                return HttpResponse("you r not allowed")
        return render(request,'login.html')