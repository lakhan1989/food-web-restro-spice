from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Post, Reservation,Contactus
from .forms import CommentsForm, ContactusForm, ReservationForm

 

# Create your views here.

def home(request):
    
    data = {}
    data["post"] = Post.objects.all()
     
    data["bakery"] = Menu.objects.filter(category__in = ['bakery', 'lunch'])[0:6] 
    data["tea"] = Menu.objects.filter(category__in = ['teas', 'coffees'])[0:6] 
    
    data["lunch"] = Menu.objects.filter(category = "lunch")[0:3]
    data["menu"] = Menu.objects.filter()
    
    return render(request, 'home.html', data)

def menu(request):
    
    data = {}
    data["tea"] = Menu.objects.filter(category__in = ['teas', 'coffees'])[0:6]
    print(data)
    data["bakery"] = Menu.objects.filter(category__in = ['bakery', 'lunch'])[0:6] 
    data["lunch"] = Menu.objects.filter(category = "lunch")[0:3] 
    data["menu"] = Menu.objects.all()
    return render(request, 'ourmenu.html', data)

def blogpost(request, id):
    
    data = {}
    data["blog"] = Post.objects.get(id=id)
    # data["filter_post"] = Post.objects.filter(post_title = "Harry Potter") 
    data["latest_news"] = Post.objects.all()[0:4]
    
    
    data["comments_form"] = CommentsForm()
     
    if request.method == 'POST':
        form = CommentsForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            data["comments_form"] = form
    
    return render(request, 'blogpost.html', data)

def comments(request):
     data ={}
     
    #  data["comments_form"] = CommentsForm()
     
    #  if request.method == 'POST':
    #     form = CommentsForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #     else:
    #         data["comments_form"] = form

     return render(request, 'comments.html', data) 
 

def contactus(request):
     
    data ={}
        
    data["contactus_form"] = ContactusForm()
    
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        
        if form.is_valid():
         form.save()
        else: 
            data["contactus_form"] = form
  
    
    return render(request, 'contact-us.html', data)


def reservation(request):

    data = {}
    data["reservation_form"] = ReservationForm()
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        
        if form.is_valid():
           form.save()
        else:
            data["reservation_form"] = form
    return render(request, "reservation.html", data)