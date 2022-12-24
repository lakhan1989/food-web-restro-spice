from django.contrib import admin
from .models import Menu, Author, Reservation, Comments, Contactus, Post

# Register your models here.

admin.site.register(Menu)
admin.site.register(Author)
admin.site.register(Reservation)
admin.site.register(Comments)
admin.site.register(Contactus)
admin.site.register(Post)