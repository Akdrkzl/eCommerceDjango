# Generated by Django 4.2.2 on 2023-07-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0005_yorum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yorum',
            name='urun',
        ),
        migrations.AddField(
            model_name='yorum',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='yorum',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
