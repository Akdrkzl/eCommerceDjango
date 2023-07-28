from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('hesap-ayarlari/', userSettings, name='usersettings'),
    path('sifre-degistir/', changePassword, name='changepassword'),
    path('eposta-degistir/', changeEmail, name='changeemail'),
    path('kullanici-adi-degistir/', changeName, name='changename'),
    path('kullaniciyi-sil/', userDelete, name='userdelete'),
]