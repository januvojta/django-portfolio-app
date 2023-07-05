from django.shortcuts import render

from users.forms import CustomUserCreationForm



def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render (request, "users/register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/register_done.html", {"form": form})
        else:
            return render(request, "users/register.html", {"form": form})