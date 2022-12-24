from django.db import models

# Create your models here.
class Menu(models.Model):
    
    CATEGORY_CHOICES = [
        ('coffees', 'Coffees'),
        ('teas', 'Teas'),
        ('bakery', 'Bakery'),
        ('lunch', 'Lunch')
    ]
    
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=200)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    
    author_name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.author_name
    
class Reservation(models.Model):
    
    persons = models.IntegerField(blank= True, null=True)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    comment = models.TextField()
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=200)
    comment = models.TextField()
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    massage = models.TextField()
    subjects = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    post_title = models.CharField(max_length=100)
    featured_image = models.ImageField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comments)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.post_title
    
    
    