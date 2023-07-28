# Generated by Django 4.2.2 on 2023-07-18 18:00

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Urunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('resimbir', models.FileField(upload_to='urunler/', verbose_name='Ürün Resmi Ön')),
                ('resimiki', models.FileField(upload_to='urunler/', verbose_name='Ürün Resmi Arka')),
                ('resimDetayBir', models.FileField(blank=True, null=True, upload_to='urunler/', verbose_name='Ürün Resmi Detay Bir')),
                ('resimDetayİki', models.FileField(blank=True, null=True, upload_to='urunler/', verbose_name='Ürün Resmi Detay İki')),
                ('resimDetayUc', models.FileField(blank=True, null=True, upload_to='urunler/', verbose_name='Ürün Resmi Detay Üç')),
                ('aciklama', ckeditor.fields.RichTextField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_home', models.BooleanField(default=False)),
                ('is_carousel', models.BooleanField(default=False)),
                ('is_look', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urunler.kategori')),
            ],
        ),
    ]
