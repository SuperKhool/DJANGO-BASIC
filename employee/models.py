from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True, max_length=254)
    photo=models.ImageField(upload_to='images')
    designation=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=11,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updatet_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name
    
    
    