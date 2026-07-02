
from django.shortcuts import render, redirect, get_object_or_404
from .models import MAC

def index(request):
    if request.method == "POST":
        MAC.objects.create(
            nomi=request.POST.get("nomi"),
            narxi=request.POST.get("narxi"),
            image_url=request.POST.get("image_url"),
        )
        return redirect("/")

    macs = MAC.objects.all()
    return render(request, "index.html", {"macs": macs})


def update(request, id):
    mac = get_object_or_404(MAC, id=id)

    if request.method == "POST":
        mac.nomi = request.POST.get("nomi")
        mac.narxi = request.POST.get("narxi")
        mac.image_url = request.POST.get("image_url")
        mac.save()
        return redirect("index")

    return render(request, "update.html", {"mac": mac})


def delete(request, id):
    mac = get_object_or_404(MAC, id=id)
    mac.delete()
    return redirect("index")