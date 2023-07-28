from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
class KategoriAdmin(admin.ModelAdmin):
    list_display = ("isim","slug",)
    readonly_fields = ("slug",)

class UrunlerAdmin(admin.ModelAdmin):
    def resimbir_preview(self, obj):
        if obj.resimbir:
            return format_html('<img src="{}" height="100px" />', obj.resimbir.url)

    list_display = ("resimbir_preview","isim","kategori","slug","renk","price","is_active","is_home","is_carousel","is_look")
    list_editable = ("is_active","is_home","is_carousel","is_look")
    readonly_fields = ("slug",)
    list_filter = ("kategori","renk","is_active","price",)

class CustomerAdmin(admin.ModelAdmin):
    list_display=("user","name","email")

class OrderAdmin(admin.ModelAdmin):
    list_display =("customer","date_orderd","complete","transaction_id")

class OrderItemAdmin(admin.ModelAdmin):
    list_display=("order","product","quantity")

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display=("order","customer","address","city","state","zipcode","date_added")



admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Urunler, UrunlerAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
