# Generated by Django 3.0.4 on 2020-04-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mask', '0006_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]