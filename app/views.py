
from django.shortcuts import render, redirect, get_object_or_404
from .models import MAC
from .models import iphone

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



def iphone_store(request):
    if request.method == "POST":
        # HTML inputlaridagi 'name' atributi orqali ma'lumotlarni tutib olamiz
        nomi = request.POST.get('nomi')
        narxi = request.POST.get('narxi')
        image_url = request.POST.get('image_url')
        
        # Ma'lumotlarni to'g'ridan-to'g'ri bazaga yangi obyekt qilib saqlaymiz
        iphone.objects.create(
            nomi=nomi,
            narxi=narxi,
            image_url=image_url
        )
        
        # Sahifa qayta yuklanganda ma'lumot ikki marta tushib ketmasligi uchun qayta yo'naltiramiz
        return redirect('iphone_store') 
    
    # Bazadagi barcha iPhone'larni olib kelamiz
    iphones = iphone.objects.all()
    
    return render(request, 'iphone.html', {'iphones': iphones})



# 2. TAHRIRLASH (Update)
def update_iphone(request, pk):
    phone = get_object_or_404(iphone, pk=pk) # ID bo'yicha telefonni topish
    
    if request.method == "POST":
        phone.nomi = request.POST.get('nomi')
        phone.narxi = request.POST.get('narxi')
        phone.image_url = request.POST.get('image_url')
        phone.save() # O'zgarishlarni saqlash
        return redirect('iphone_store')
        
    return render(request, 'update_uphone.html', {'phone': phone})


# 3. O'CHIRISH (Delete)
def delete_iphone(request, pk):
    phone = get_object_or_404(iphone, pk=pk)
    phone.delete() # Bazadan o'chirish
    return redirect('iphone_store') 