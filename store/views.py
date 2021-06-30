from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Product, Contact, Order, OrderUpdate
from math import ceil

import logging
import json

logger = logging.getLogger(__name__)


def home(request):
  return render(request, 'store/home.html')


def store(request):
  # products = Product.objects.all()
  # n = len(products)
  # noOfSlides = n // 4 + ceil((n / 4) + (n // 4))

  # context = {'product':products, 'noOfSlides':noOfSlides, 'range':range(1, noOfSlides)}
  productAll = []
  productCategory = Product.objects.values('category', 'id')
  categories = {item['category'] for item in productCategory}
  for category in categories:
    products = Product.objects.filter(category=category)
    n= len(products)
    noOfSlides = n // 4 + ceil((n / 4) - (n // 4))
    productAll.append([products, range(1, noOfSlides), noOfSlides])

  context = {'productAll':productAll}
  return render(request, 'store/store.html', context)


def search(request):
  query = request.GET.get('search')
  productAll = []
  productCategory = Product.objects.values('category', 'id')
  categories = {item['category'] for item in productCategory}
  for category in categories:
    prod = Product.objects.filter(category=category)
    products =[item for item in prod if searchProduct(query, item)]
    n= len(products)
    noOfSlides = n // 4 + ceil((n / 4) - (n // 4))
    if len(products) != 0:
      productAll.append([products, range(1, noOfSlides), noOfSlides])
  
  context = {'productAll':productAll, "msg": ""}
  if len(productAll) == 0:
    context = {"msg":"No Search Results Found!"}
  return render(request, 'store/search.html', context)


def searchProduct(query, item):
  if query in item.productName.lower() or query in item.description.lower() or query in item.category.lower():
    return True
  else:
    return False


def about(request):
  return render(request, 'store/about.html')


def contact(request):
  thank=False
  if request.method == "POST":
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    description = request.POST.get('description', '')
    contact= Contact(name=name, email=email, phone=phone, description=description)
    contact.save()
    thank=True
  context = {'thank':thank}
  return render(request, 'store/contact.html', context)


def tracker(request):
  if request.method == "POST":
    orderId = request.POST.get('orderId', '')
    email = request.POST.get('email', '')
    try:
      order = Order.objects.filter(orderId=orderId, email=email)
      if len(order) > 0:
        update = OrderUpdate.objects.filter(orderId=orderId)
        orderUpdates = []
        for item in update:
          orderUpdates.append({'text': item.updateDescription, 'time': item.timeStamp})
          # response = json.dumps([orderUpdates, order[0].itemsJson], default=str)
          response = json.dumps({"status":"success", "updates": orderUpdates, "itemJson" : order[0].itemsJson}, default=str)
        return HttpResponse(response)
      else:
        return HttpResponse('{}')
    except:
        return HttpResponse('{}')

  return render(request, 'store/tracker.html')


def productInfo(request, id):
  product = Product.objects.filter(id=id)
  print(product)
  context = {'product':product[0]}
  return render(request, 'store/productInfo.html', context)


def checkout(request):
  if request.method == "POST":
    itemsJson = request.POST.get('itemsJson', '')
    name = request.POST.get('name', '')
    amount = request.POST.get('amount', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    address = request.POST.get('address', '')
    city = request.POST.get('city', '')
    state = request.POST.get('state', '')
    zipCode = request.POST.get('zipCode', '')
    order = Order(itemsJson=itemsJson, name=name, amount=amount, email=email, phone=phone,address=address, city=city, state=state, zipCode=zipCode)
    order.save()
    update = OrderUpdate(orderId=order.orderId, updateDescription="Order Has Been Placed Successfully!")
    update.save()
    thank=True
    id=order.orderId

    return render(request, 'store/checkout.html', {'thank':thank, 'id':id})
  return render(request, 'store/checkout.html')
