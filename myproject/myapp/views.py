from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
# Create your views here.

# def home(request):
#     return HttpResponse("Hello This is my first web page")


def home(request):
    
    return render(request, "myapp/home.html")

# def form_view(request):
#     form=forms.Registerform
#     if request.method=="POST":
#         form=forms.Registerform(request.POST)
#         if form.is_valid():
#             print("validation worked")
#             print("Name :" + form.cleaned_data['first_name'])
#             print("Last_name" + form.cleaned_data['last_name'])
#             print("email " + form.cleaned_data['email'])

  
#     return render(request, 'myapp/index.html', {'form':form})




def create(request):
    if request.method=="POST":
        form=forms.Registerform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("success")
            except:
                print("error saving")
    else:
        form=forms.Registerform()
    return render(request, 'myapp/index.html', {'form':form})



def success(request):
    return render(request,'myapp/success.html')

