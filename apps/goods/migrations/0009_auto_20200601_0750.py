# Generated by Django 2.2.10 on 2020-06-01 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20170826_1201'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='goodscategorybrand',
            table='goods_goodsbrand',
        ),
    ]