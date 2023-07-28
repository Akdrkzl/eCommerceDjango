from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from .models import *
import json
import datetime

# Create your views here.


def index(request,):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    kategori = Kategori.objects.all()
    carousel = Urunler.objects.filter(is_carousel=True)
    urun = Urunler.objects.filter(is_home=True, is_active=True,)
    
    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        urun = Urunler.objects.filter(
            Q(isim__icontains = search) |
            Q(renk__icontains = search) |
            Q(kategori__isim__icontains = search) |
            Q(price__icontains = search) 
        )
    
    context = {
        'urun' : urun,
        'kategori' : kategori,
        'carousel' : carousel,
        'cartItems' : cartItems,
    }
    return render(request, 'index.html',context)

def products(request,slug):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cartItems = order['get_cart_items']

    urun = Urunler.objects.filter(is_active=True, kategori__slug = slug)
    kategori = Kategori.objects.all()
    secilenKategori = slug
    context={
        'urun' : urun,
        'kategori' : kategori,
        'secilenKategori': secilenKategori,
        'cartItems' : cartItems,
    }
    return render(request, 'products.html',context)

def productDetial(request, slug):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cartItems = order['get_cart_items']

    detay = Urunler.objects.filter(slug = slug)
    look = Urunler.objects.filter(is_active=True, is_look=True)
    kategori = Kategori.objects.all()
    context ={
        'detay' : detay,
        'kategori' : kategori,
        'look' : look,
        'cartItems' : cartItems,
    }
    return render (request,'productdetail.html', context)


def bodyCalculate(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cartItems = order['get_cart_items']

    kategori = Kategori.objects.all()
    context ={
        'kategori' : kategori,
        'cartItems' : cartItems,
    }
    return render (request, 'bodycalculate.html', context)

def basket(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    kategori = Kategori.objects.all()
    context = {
        'kategori' : kategori,
        'items' : items,
        'order' : order,
        'cartItems' : cartItems,
    }
    return render(request,'basket.html',context)

def kontrolEt(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0}

    kategori = Kategori.objects.all()
    context = {
        'kategori' : kategori,
        'items' : items,
        'order' : order,
    }
    return render(request,'kontrol.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Urunler.objects.get(id=productId)
    order , created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0 :
        orderItem.delete()
    
    if action == 'delete':
        orderItem.delete()

    return JsonResponse('Item was add', safe=False)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

    else:
        print('kulanıcı giriş yapmadı')
    return JsonResponse('Odeme Tamamlandi', safe=False)

