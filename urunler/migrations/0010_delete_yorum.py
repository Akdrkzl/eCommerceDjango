# Generated by Django 4.2.2 on 2023-07-21 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0009_alter_yorum_urun'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Yorum',
        ),
    ]