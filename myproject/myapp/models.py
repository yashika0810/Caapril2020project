from django.db import models

# Create your models here.

#name of table--> model(class)
#fields of my table--> attributes of class￼

class Signup(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Session(models.Model):
    session=models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.session
    
class Student(models.Model):
    name=models.CharField(max_length=50,unique=False)
    session=models.ForeignKey("Session", on_delete=models.PROTECT)



class Register(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    verify_email=models.EmailField(max_length=50)
   
   
    def __str__(self):
       return self.first_name
       