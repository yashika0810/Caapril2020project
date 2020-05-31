from django import forms
from django.core import validators
from .models import Register
from django.forms import ModelForm


class Registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"
        

    

   




#    def check(value):
#     if value[0].lower()!='a':
#         raise forms.ValidationError("Name should start with a")

# def valid(password):
#     if len(password)>5:
#         raise forms.ValidationError("please enter less than 5 characters")

#     def clean(self):
#         email=self.cleaned_data['email']
#         vemail=self.cleaned_data['verify_email']
#         if email!=vemail:
#             raise forms.ValidationError("email doesn't match")

        
  
 