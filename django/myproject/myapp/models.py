from django.db import models    

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length=100)
    time_registr = models.DateField()



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10,decimal_places=10)
    quantity = models.IntegerField()
    date = models.DateTimeField()


# class Order(models.Model):
#     customer = models.ForeignKey()
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     age = models.IntegerField()



