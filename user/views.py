from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout

from user.authentication import AccountAuthentication
from user.models import Account

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        account_model = Account.objects.create(
            first_name=request.POST['first-name'],
            last_name=request.POST['last-name'],
            username=request.POST['username'],
            email=request.POST['email'],
        )
        account_model.set_password(request.POST['password1'])
        account_model.save()
        user = AccountAuthentication.authenticate(request, username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
        login(request, user)
        return redirect('dashboard')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        user = AccountAuthentication.authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login-view')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login-view')
        
