from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from urunler.models import *

# Create your views here.
def userRegister(request):
    kategori = Kategori.objects.all()
    context = {
        'kategori' : kategori,
    }
    if request.method == 'POST':
        isim = request.POST['isim']
        soyisim = request.POST['soyisim']
        email = request.POST['email']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if sifre1 == sifre2:
            if User.objects.filter(email = email).exists():
                messages.error(request,'Bu Mail Adresi Zaten Kullanılıyor.')
                return redirect('register')
            else:
                user = User.objects.create_user(username =  email, email = email, first_name = isim, last_name = soyisim, password = sifre1)
                customer = Customer.objects.create(user = user, name = isim, email = email)
                customer.save()
                user.save()
                messages.success(request, 'Kullanıcı Oluşturuldu')
                return redirect('login')
        else:
            messages.error(request,'Şifreler Eşleşmiyor.')
            return redirect('register')
    else:
        return render(request,'register.html',context)


def userLogin(request):
    kategori = Kategori.objects.all()
    context = {
        'kategori' : kategori,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request,'Giriş Başarılı.')
            nextUrl = request.GET.get('next', None)
            if nextUrl is None:
                return redirect('index')
                messages.success(request,'Giriş Başarılı.')
            else:
                return redirect(nextUrl)
                messages.success(request,'Giriş Başarılı.')
        else:
            messages.error(request,'Kullanıcı adı veya şifre yanlış.')
            return redirect('login')
    return render(request,'login.html',context)


def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı')
    return redirect('login')

@login_required(login_url='login')
def userSettings(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cartItems = order['get_cart_items']
    kategori = Kategori.objects.all()
    context = {
        'kategori' : kategori,
        'cartItems' : cartItems,
    }
    return render (request, 'accountsettings.html',context)

@login_required(login_url='login')
def changePassword(request):
    if request.method == 'POST':
        currentPassword = request.POST['currentPassword']
        newPassword1 = request.POST['newPassword1']
        newPassword2 = request.POST['newPassword2']

        user = request.user
        if user.check_password(currentPassword):
            if newPassword1 == newPassword2:
                user.set_password(newPassword1)
                user.save()
                update_session_auth_hash(request,user)
                messages.success(request,'Şifre Başarılı Bir Şekilde Değiştirildi')
                return redirect('usersettings')
        else:
            messages.error(request,'Mevcut Şifre Yanlış veya Yeni Şifreler Eşleşmiyor.')
            return redirect('changepassword')
    return render (request,'changepassword.html')

@login_required(login_url='login')
def changeEmail(request):
    if request.method == 'POST':
        newEmail= request.POST['newEmail']

        if User.objects.filter(email = newEmail).exists():
            messages.error(request,'Bu Mail Adresi Zaten Kullanılıyor.')
            return redirect('changeemail')
        else:
            user = request.user
            user.email = newEmail
            user.save()
            update_session_auth_hash(request,user)
            messages.success(request,'E-posta Bir Şekilde Değiştirildi')
            return redirect('usersettings')
    return render(request, 'changeemail.html')

@login_required(login_url='login')
def changeName(request):
    if request.method == 'POST':
        newName = request.POST['newName']
        newLastName = request.POST['newLastName']

        user = request.user
        user.first_name = newName
        user.last_name = newLastName
        user.save()
        messages.success(request,'Kullanıcı Adı Başarıyla Değiştirildi')
        return redirect('usersettings')
    return render(request, 'changename.html')

def userDelete(request):
    user = request.user
    user.delete()
    messages.success(request, 'Hesabınız Silindi')
    return redirect('index')