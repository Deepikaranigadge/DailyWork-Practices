from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from product.models import Product 
from .models import Profile
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    templates = 'index.html'

    product_list = Product.objects.all()

    return render(request, templates, {'products': product_list})

def register(request):
    if request.method =='POST':
      email = request.POST.get('email', '')
      name = request.POST.get('name', '')
      password = request.POST.get('password', '')
   
      user = User.objects.create_user(email, email, password)
      user.first_name = name

      user.save()
      return HttpResponse('Succesully Registered!!')

    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile_page") 

    return render(request, "login.html")

def logout_page(request):
   logout(request)
   return redirect('home')


@login_required(login_url="/login/")
def profile_page(request):
   if request.method == 'POST':
       first_name = request.POST.get('first_name', '')
       last_name = request.POST.get('last_name', '')
       address = request.POST.get('address', '')
       phone_number = request.POST.get('phone_number', '')

       request.user.first_name = first_name
       request.user.last_name = last_name
       request.user.save()

       user_profile = Profile.objects.filter(user=request.user)

       user_profile.update(address = address,
                            phone = phone_number)
       
       print("======>1",user_profile[0].phone)

   user_profile_data = Profile.objects.get(user=request.user)
   print("======>2",user_profile_data.phone) 
   context = {"user_profile":user_profile_data}

   return render(request, 'profile.html', context)

#def login_page(request):
   #if request.method == 'POST':   
      #email = request.POST.get('email', '')
      #password = request.POST.get('password', '') 
      #user = authenticate(request, username=email, password=password)
      #if user is not None:
         #login(request, user)
         #return redirect('home')
      

      #return render(request, 'login.html')
   

   

   





