# Generated by Django 3.0.4 on 2020-04-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mask', '0003_auto_20200411_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('L', 'L'), ('M', 'M'), ('S', 'S')], max_length=30, null=True),
        ),
    ]