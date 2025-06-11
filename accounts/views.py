from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, SignupForm


def signup_view(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.save()
            return redirect("accounts:login")
    else:
        signup_form = SignupForm()
    return render(request, "signup.html", {"signup_form": signup_form})


def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data["email"]
            password = login_form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("stockmarket_news:news_list")
            else:
                login_form.add_error(None, "Invalid email or password")
    else:
        login_form = LoginForm()
    return render(request, "login.html", {"login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")
