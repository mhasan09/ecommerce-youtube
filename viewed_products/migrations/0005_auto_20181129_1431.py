# Generated by Django 2.1 on 2018-11-29 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewed_products', '0004_auto_20181129_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewed_product',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
