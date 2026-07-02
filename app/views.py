from django.shortcuts import render
from app.models import MAC

# Create your views here.


from django.shortcuts import render, redirect
from .models import MAC

def index(request):
    if request.method == "POST":
        MAC.objects.create(
            nimi=request.POST.get("nimi"),
            narxi=request.POST.get("narxi"),
            image_url=request.POST.get("image_url"),
        )
        return redirect("/")

    macs = MAC.objects.all()
    return render(request, "index.html", {"macs": macs})