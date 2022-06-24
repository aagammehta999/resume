from email import message
from django import forms
from .models import ContactProfile

class ContactForm(forms.ModelForm):
    
    name=forms.CharField(max_length=100,required=True,
                         widget=forms.TextInput(attrs={
                                'placeholder':'*Full Name',
                                'class':'form-control'
                                }))
    
    email=forms.EmailField(required=True,max_length=254,
                           widget=forms.EmailInput(attrs={
                               'placeholder':'*Email',
                               'class':'form-control'
                           }))
    
    message=forms.CharField(required=True,max_length=1000,
                            widget=forms.Textarea(attrs={
                                'placeholder':'*Message',
                                'rows':'5',
                            }))
    
    
    class Meta:
        model=ContactProfile
        fields=['name','email','message']