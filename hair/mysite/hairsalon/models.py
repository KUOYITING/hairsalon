from django.db import models

# Create your models here.
class Item(models.Model):
    itemName = models.CharField(max_length=20, unique=True)
    itemPrice = models.DecimalField(max_digits=4, decimal_places=1)
    itemCost = models.DecimalField(max_digits=4, decimal_places=1)
    itemQuantity = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.itemName


class Service(models.Model):
    serviceName = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.serviceName

class Designer(models.Model):
    designerName = models.CharField(max_length=20, unique=True)
    experience = models.DecimalField(max_digits=3, decimal_places=1)
    level = models.CharField(max_length=3)
    salary = models.DecimalField(max_digits=10, decimal_places=1)
    workinghour = models.CharField(max_length=20)
    dayoff = models.CharField(max_length=20)

    def __str__(self):
        return self.designerName

class bookingItem(models.Model):
    itemID = models.DecimalField(max_digits=20, decimal_places=0, unique=True)
    name = models.CharField(max_length=20)
    phone = models.DecimalField(max_digits=15, decimal_places=0)
    itemName = models.CharField(max_length=20)
    orderQuantity = models.DecimalField(max_digits=2, decimal_places=0)
    orderPrice = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.itemID