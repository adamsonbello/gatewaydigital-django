# Generated by Django 4.0.5 on 2022-07-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_description_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
    ]
