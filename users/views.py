from django.shortcuts import redirect, render
from caps.models import Cap
from caps.views import index
from users.models import CustomUser
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as logout_user
# Create your views here.

def register_name(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser(first_name=first_name, last_name=last_name,username=username, gender=gender, phone_number=phone_number,email=email,password=password)
        user.set_password(password)

        user.save()
        return render(request,'login.html',{'message':'user created successfully'})
    return render(request,'register.html',{'message':'method not allowed'})



def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['id'] = CustomUser.objects.get(username=username).id
            request.session['username'] = username
            return redirect(index)

        else:
            return render(request,'login.html',{'message':'credentials mismatched'})
    else:
        return render(request, 'login.html')



def show_user_details(request):
    id  = request.user.id
    user = CustomUser.objects.get(id=id)
    male, female, others = None, None, None
    if user.gender=='Male':
            male=True
    elif user.gender=='Female':
        female=True
    else:
        others=True
    return render(request, "show_details.html", {'users':user, 'male':male, 
                                                 'female':female, 'others':others})

def update_user(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method=="POST":
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.gender = request.POST['gender']
        user.username = request.POST['username']
        user.phone_number =request.POST['phone_number']
        user.email = request.POST['email']
        user.save()
    return redirect(show_user_details)    
        
def logout(request):
    logout_user(request)
    return redirect(index)

def update_password(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method=="POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
    return redirect(index) 

def delete_user(request, id):
    CustomUser.objects.get(id=id).delete()
    return redirect(index)
    

            


    


        
