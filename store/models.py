from django.db import models

class Product(models.Model):
  productId = models.AutoField
  productName = models.CharField(max_length=50)
  category = models.CharField(max_length=30, default="")
  subcategory = models.CharField(max_length=30, default="")
  price = models.IntegerField(default=0)
  description = models.CharField(max_length=200)
  publishDate = models.DateField()
  image = models.ImageField(default="")

  def __str__(self):
    return self.productName

class Contact(models.Model):
  msgId = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, default="")
  email = models.CharField(max_length=50, default="")
  phone = models.CharField(max_length=50, default="")
  description = models.CharField(max_length=500, default="")

  def __str__(self):
    return self.email

class Order(models.Model):
  orderId = models.AutoField(primary_key=True)
  itemsJson = models.CharField(max_length=1000)
  amount = models.IntegerField(default=0)
  name = models.CharField(max_length=60)
  email = models.CharField(max_length=60)
  phone = models.CharField(max_length=20)
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipCode = models.CharField(max_length=60)

  def __str__(self):
    return self.name


class OrderUpdate(models.Model):
  updateId = models.AutoField(primary_key=True)
  orderId = models.IntegerField(default="")
  updateDescription = models.CharField(max_length=100)
  timeStamp = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.updateDescription[0:10] + "..."
