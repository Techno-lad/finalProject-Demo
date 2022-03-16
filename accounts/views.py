from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is None:
            if username == "Wright" and password == "1234":
                auth.login(request, user)
                return redirect("lect")
            else:
                auth.login(request, user)
                return redirect("dash")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")
    else:

        return render(
            request, "login.html"
        )  # can pass user object in params to use in the login


def register(request):
    if (
        request.method == "POST"
    ):  # 1st if block simply assigns attributes via post method, so assigns values and checks if they are done via post method
        id = request.POST["id"]
        firstName = request.POST["first_name"]
        lastName = request.POST["last_name"]
        username = request.POST["username"]  # username might need to be user_name
        email = request.POST["email"]
        password = request.POST["password1"]
        confirmPassword = request.POST["password2"]

        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username is already taken")
                return redirect("register")
            elif User.objects.filter(id=id).exists():
                messages.info(request, "id is already taken")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    id=id,
                    first_name=firstName,
                    last_name=lastName,
                )
                user.save()
                messages.info(request, "new user created")
                return redirect("login")

        else:
            messages.info(request, "password is not matching")
            return redirect("register")
        # return redirect('/')                   recently commented out this line
        # this redirects to home or you could just redirect to login your choice
    else:
        return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("login")
