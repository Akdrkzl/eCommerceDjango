# Generated by Django 4.2.2 on 2023-07-21 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0008_alter_yorum_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorum',
            name='urun',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='urunler.urunler'),
        ),
    ]
