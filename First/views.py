from django.http import HttpResponse
from django.shortcuts import render,redirect
from service.models import Booking
from Chef.models import Chef
from Menu.models import Menu

def aboutUs(request):
    return HttpResponse("Hello World")


def detail(request,courseid):
    return HttpResponse(courseid)


def saveBooking(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('datetime')  # Correct the field name
        people = request.POST.get('select1')
        message = request.POST.get('message')

        # Create a Booking object and save it
        booking = Booking(name=name, email=email, dateTime=date, peoples=people, specialrequest=message)
        booking.save()


    return render(request, "booking.html")








# def saveBooking(request):
    
#     if request.method=="POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         date=request.POST.get('datatime')
#         people=request.POST.get('select1')
#         message=request.POST.get('message')        
    
#     en=Booking(name=name,email=email,dateTime=date,peoples=people,specialrequest=message).save()
#     return render(request,"booking.html")
    


def homePage(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


def booking(request):
    return render(request,"booking.html")

def menu(request):
    
    menu=Menu.objects.all()
    
    data={
        'menu':menu
    }
    return render(request,"menu.html",data)

def service(request):
    return render(request,"service.html")

def team(request):
    
    team=Chef.objects.all()
    
    data={
        'team':team
    }
    return render(request,"team.html",data)

def contact(request):
    return render(request,"contact.html")

def testimonial(request):
    return render(request,"testimonial.html")




def adminPanel(request):
    return render(request,"admin.html")


def viewBookings(request):
    bookings=Booking.objects.all()
    
    data={
        'bookings':bookings
    }
    return render(request,"viewBookings.html",data)



def viewChefs(request):
    team=Chef.objects.all()
    
    data={
        'team':team
    }
    return render(request,"View_Chef.html",data)


def AddChefs(request):
    if request.method == "POST":
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        image = request.FILES.get('file')  # Correct the field name
        
        # Create a Booking object and save it
        chef = Chef(name=name,designation=designation,image=image)
        chef.save()


    return render(request,"Add_Chef.html")



def chef(request):
    return render(request,"Add_Chef.html")
