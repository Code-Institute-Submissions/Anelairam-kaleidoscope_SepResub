# Generated by Django 4.1 on 2022-09-23 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_difficulty_remove_event_level_delete_level_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='difficulty',
            options={'verbose_name_plural': 'Difficulties'},
        ),
    ]