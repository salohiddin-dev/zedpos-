# Generated by Django 4.2.1 on 2023-06-06 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='measure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.measure'),
        ),
    ]
