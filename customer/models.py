from django.db import models

# Create your models here.
class customer(models.Model):
    first_name=models.CharField(max_length=15,null=True,blank=True)
    last_name=models.CharField(max_length=15,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    country=models.CharField(max_length=20,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    dob=models.CharField(max_length=20,null=True,blank=True)

    def str_(self):
        return self.first_name
    
class Customer_Address(models.Model):
    customer= models.ForeignKey(customer,on_delete =models.CASCADE,null=True,blank=True,related_name="customer_address")
    street_name=models.CharField(max_length=15,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    state=models.CharField(max_length=20,null=True,blank=True)
    country=models.CharField(max_length=20,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=20,null=True,blank=True)

    def str_(self):
        return self.street_name
    
    
class Customer_Adhar(models.Model):
    customer= models.OneToOneField(customer,on_delete =models.CASCADE)
    adhar_name=models.CharField(max_length=15,null=True,blank=True)
    adhar_no=models.IntegerField(null=True,blank=True)

    def str_(self):
        return self.adhar_name
    

