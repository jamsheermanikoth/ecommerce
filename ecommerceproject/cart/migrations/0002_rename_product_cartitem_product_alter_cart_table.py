# Generated by Django 4.1.5 on 2023-03-09 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='Product',
        ),
        migrations.AlterModelTable(
            name='cart',
            table='Cart',
        ),
    ]
