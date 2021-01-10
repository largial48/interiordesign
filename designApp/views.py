from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item,system,contact
from django.db.models import Q
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def contact_us(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        con = contact(contact_name=name,contact_email=email,contact_message=message)
        con.save()
        messages.success(request,"Your message is submitted succesfully !")
        return redirect('index')

    return render(request,'contact.html')

def items(request):
    jmbtrns = item.objects.all()
    lists = {"items":jmbtrns}

    if request.method == "POST":
        txt = request.POST["search"]
        if txt == 'all' or txt == 'All':
            return render(request,'items.html',lists)

        jmbtrns = item.objects.filter(Q(item_name__icontains=txt) | Q(item_desc__icontains=txt) | Q(item_category__icontains=txt))
        lists = {"items": jmbtrns}
    return render(request,'items.html',lists)

def systems(request):
    systems = system.objects.all()
    lists = {'systems':systems}
    
    if request.method == "POST":
        search = request.POST["search"]
        if search == 'all' or search == 'All':
            return render(request,'systems.html',lists)

        systems = system.objects.filter( Q(system_name__icontains=search) | Q(system_desc__icontains=search) | Q(system_category__icontains=search) | Q(system_feature__icontains=search) )
        lists = {'systems':systems}
        return render(request,'systems.html',lists)
    return render(request,'systems.html',lists)

def systemView(request,id=0):
    sys = system.objects.get(id=id)
    lists = {'system': sys}
    return render(request,'systemView.html',lists)

# Django Admin SuperUser details = Name: shivam , Password: shivam
# Please checkout contacts table in admin panel 