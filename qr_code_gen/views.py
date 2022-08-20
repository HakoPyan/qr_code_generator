from multiprocessing import context
from django.shortcuts import render, redirect
import qrcode
from qr_code_gen.models import QR_Data

from .forms import QR_DataForm

# Create your views here.
def qr_form(request):
    form = QR_DataForm()
    if request.method == "POST":
        form = QR_DataForm(request.POST)
        if form.is_valid():
            form.save()
            qrcode_img = qrcode.make(QR_Data.objects.last())
            fname = fr"C:\Users\USER\Desktop\django-project\media\{request.POST['phone_number']}.png"
            qrcode_img.save(fname)
            return redirect('show_qr')
        else:
            form = QR_DataForm()
    context = {"form" : form}
    return render(request, "form.html", context)

def show_qr(request):
    img = f"../media/{QR_Data.objects.last().phone_number}.png"
    context = {"img": img}
    return render(request, "qr.html", context)

def add_qr(request):
    last = QR_Data.objects.last()
    last.qr = f"../media/{QR_Data.objects.last().phone_number}.png"
    last.save()
    data = QR_Data.objects.all()
    context = {'data': data}
    return render(request, "main.html", context)