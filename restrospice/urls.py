from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('comments/', views.comments, name='comments'),
    path('blogpost/<int:id>/', views.blogpost, name='blogpost'),
    path('contactus/', views.contactus, name='contactus'),
    path('reservation/', views.reservation, name='reservation')
]