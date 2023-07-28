from django.urls import path
from urunler.views import *

urlpatterns = [
    path('', index, name='index'),
    path('ürünler/<slug:slug>', products, name='ürünler'),
    path('üründetay/<slug:slug>', productDetial, name='üründetay'),
    path('beden-hesaplama/', bodyCalculate, name='bodycalculate'),
    # sepet-işlemleri
    path('sepet/', basket, name='sepet'),
    path('kontrol/', kontrolEt, name='kontrol'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),

]