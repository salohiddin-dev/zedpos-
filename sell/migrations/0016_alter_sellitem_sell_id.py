# Generated by Django 4.2.1 on 2023-06-06 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0015_sell_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellitem',
            name='sell_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sell.sell'),
        ),
    ]
