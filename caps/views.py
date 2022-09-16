import re
from django.shortcuts import redirect, render,HttpResponse
from pyrsistent import b
from caps.models import Cap, Order
from users.models import CustomUser


# Create your views here.
def index(request):
    caps = Cap.objects.all()
    return render(request, 'caps.html', {'data':caps})

def about(request):
    return render(request, 'about.html', {})


def login(request):
    return render(request,'login.html',{})

def register(request):
    return render(request,'register.html',{})

def most_viewed(request):
    caps = Cap.objects.all()
    return render(request, 'most_viewed.html', {'dara':caps})

def best_seller(request):
    caps = Cap.objects.all()
    return render(request, 'best_seller.html', {'data':caps})

def latest_arrivals(request):
    caps = Cap.objects.all()
    return render(request, 'latest_arrivals.html', {'data':caps})

def create_caps(request):
    if request.user.is_superuser:
        if request.method=="POST" :
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            get_pictures = request.FILES.get('file')
            model = Cap(name=name, image=get_pictures, desc=description,
                price=price)
            model.save()
            return render(request, 'create_caps.html', {'message':"data is stored successfully"})
    
        return render(request,'create_caps.html', {'message':'problem storing the data'})



def show_caps(request,id=None):
    if request.method=="GET":
        if id:
            cap = Cap.objects.get(id=id)
            return render(request, 'show_caps.html', {'data':cap})
        caps = Cap.objects.all()
        return render(request, 'show_caps.html', {'data':caps})
    return render(request,'create_caps.html', {'message':'problem fetching the data'})


def cap_details(request, id):
    cap = Cap.objects.get(id=id)

    return render(request, "cap_details.html", {'cap':cap})

def update_cap(request,id):
    if request.user.is_superuser:
        cap = Cap.objects.get(id=id)
        if request.method=="POST":
            cap.name = request.POST['name']
            get_pictures = request.FILES.get('file')
            cap.image = get_pictures
            cap.desc = request.POST['desc']
            cap.price =request.POST['price']
            cap.save()
        return redirect(cap_details,id=id) 

def delete_cap(request,id):
    cap = Cap.objects.get(id=id).delete()
    return redirect(index)
    
def create_order(request,id):
    if request.method=="POST":
        cap = Cap.objects.get(id=id)
        id  = request.user.id
        user = CustomUser.objects.get(id=id)
        quantity = request.POST['quantity']
        total_price = int(quantity) * cap.price
        model = Order(cap=cap,user=user,total_price=total_price,quantity=quantity)
        model.save()
        return redirect(index)
    
    return render(request,'caps.html', {'message':'Problem placing the order'})

def cart(request):
    order = Order.objects.filter(user=request.user)
    sum = 0
    for i in order:
        sum+=i.total_price
    return render(request,'cart.html', {'orders':order, 'length':len(order),'sum':sum})

def proceed_payment(request):
    return HttpResponse("Your Request Has Been Submitted.... It will be deliver in two days")
