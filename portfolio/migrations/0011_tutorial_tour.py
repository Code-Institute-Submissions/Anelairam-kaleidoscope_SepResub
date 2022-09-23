# Generated by Django 4.1 on 2022-09-20 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_remove_product_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('duration', models.DurationField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.category')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.type')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.category')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.type')),
            ],
        ),
    ]