# Generated by Django 4.1 on 2022-09-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
