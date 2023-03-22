from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from homescreen.forms import AccountUpdateForm, RegistrationForm, AccountAuthenticationForm, UserLoginForm


def home_screen_view(request):
    context = {}
    return render(request, "home.html", context)


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        print(form)
        for filed in form:
            print(filed)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(request, username=username, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = UserLoginForm()

    context['login_form'] = form

    return render(request, "account/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(

            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context['account_form'] = form
    context['blog_posts'] = ""

    return render(request, "account/account.html", context)
