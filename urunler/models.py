from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Kategori(models.Model):
    isim = models.CharField(max_length=50)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isim

class Urunler(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE) 
    isim = models.CharField(max_length=100)
    renk = models.CharField(max_length=50, null=True, blank=True)
    resimbir = models.FileField(upload_to='urunler/', verbose_name='Ürün Resmi Ön')
    resimiki = models.FileField(upload_to='urunler/', verbose_name='Ürün Resmi Arka')
    resimDetayBir = models.FileField(null=True, blank=True, upload_to='urunler/', verbose_name='Ürün Resmi Detay Bir')
    resimDetayİki = models.FileField(null=True, blank=True, upload_to='urunler/', verbose_name='Ürün Resmi Detay İki')
    resimDetayUc = models.FileField(null=True, blank=True, upload_to='urunler/', verbose_name='Ürün Resmi Detay Üç')
    aciklama = RichTextField()
    price = models.IntegerField()
    quantity = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    is_carousel = models.BooleanField(default=False)
    is_look = models.BooleanField(default=False)
    digital = models.BooleanField(default=False, null=True, blank=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isim

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Urunler, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)

