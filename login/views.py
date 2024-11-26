from django.shortcuts import render, redirect
# # import cx_Oracle

from .models import User

em = ""
pwd = ""


# Create your views here.
def loginaction(request):
    if request.method == "POST":
        email = request.POST.get("lemail")
        password = request.POST.get("lpsw")

        try:
            user = User.objects.get(email=email, password=password)
            request.session["islogged"] = True
            return render(
                request,
                "login_page.html",
                {
                    "loggedin": request.session["islogged"],
                    "name": f"{user.firstname} {user.lastname}",
                },
            )
        except User.DoesNotExist:
            return render(
                request,
                "login_page.html",
                {"openlogin": True, "msg": "Invalid Credentials"},
            )

    return render(request, "login_page.html")


def aboutusaction(request):
    return render(request, "aboutus.html")


def logout(request):
    request.session["islogged"] = False
    return redirect("/login")


def signup_login(request):
    return render(request, "login_page.html", {"openlogin": True})
