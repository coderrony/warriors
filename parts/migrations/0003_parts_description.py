# Generated by Django 4.1.7 on 2023-03-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0002_rename_car_image_parts_part_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
