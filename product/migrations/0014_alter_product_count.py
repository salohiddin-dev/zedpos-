# Generated by Django 4.2.2 on 2023-07-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]