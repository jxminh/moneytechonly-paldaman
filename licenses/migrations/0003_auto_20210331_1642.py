# Generated by Django 3.1.7 on 2021-03-31 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0002_auto_20210331_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='product_ordrer_number',
            new_name='product_order_number',
        ),
    ]