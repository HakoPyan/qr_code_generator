from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from qr_code_gen.models import QR_Data


# Create your views here.
def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('qr_form')
        else:
            form = UserCreationForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context)


def main(request):
    data = QR_Data.objects.all()
    context = {'data': data}
    return render(request, "main.html", context)


def qr_form(request):
    return render(request, "form.html")