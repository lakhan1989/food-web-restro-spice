from django.forms import ModelForm
from .models import Comments, Reservation, Contactus
from django import forms

class CommentsForm(ModelForm):
    
    class Meta:
        model = Comments
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs={'class': 'reply-input'} 
        self.fields['email'].widget.attrs={'class': 'reply-input'}
        self.fields['website'].widget.attrs={'class': 'reply-input'}
        self.fields['comment'].widget.attrs={'class': 'reply-input', 'cols':'76', 'rows':'9'}
    
    
class ContactusForm(ModelForm):
    
    class Meta:
        model = Contactus
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(ContactusForm, self).__init__(*args, **kwargs) 
        self.fields['name'].widget.attrs={'class': 'your-name-input'} 
        self.fields['email'].widget.attrs={'class': 'your-name-input', 'style': '190%'}
        self.fields['massage'].widget.attrs={'class': 'contact-textarea', 'cols':'76', 'rows':'9'}
        self.fields['subjects'].widget.attrs={'class': 'your-name-input'}
        
class ReservationForm(ModelForm):
    
    
    PERSONS_CHOICES = (
        ("1", "1 Person"), 
        ("2", "2 Person"), 
        ("3", "3 Person"),
        ("4", "4 Person"),
        ("5", "5 Person")
    )
    persons = forms.ChoiceField(choices = PERSONS_CHOICES)
    
    
    class Meta:
        model = Reservation
        fields = "__all__"
        
        
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        
        self.fields['persons'].widget.attrs={'class': 'table-content', 'placeholder':'Persons'  }
        self.fields['date'].widget.attrs={'class': 'table-content', 'placeholder':'yyyy-mm-dd'}
        self.fields['time'].widget.attrs={'class': 'table-content', 'placeholder':'hh:mm:ss'}
        self.fields['name'].widget.attrs={'class': 'table-content', 'placeholder':'Name'}
        self.fields['email'].widget.attrs={'class': 'table-content', 'placeholder':'Email'}
        self.fields['phone'].widget.attrs={'class': 'table-content', 'placeholder':'Phone'}
        self.fields['comment'].widget.attrs={'class': 'table-textarea', 'placeholder':'Comment', 'cols':'76', 'rows':'6'} 
 
        
        
   
   
   
  
  
