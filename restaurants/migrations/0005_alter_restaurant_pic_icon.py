# Generated by Django 3.2.5 on 2021-07-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_alter_restaurant_pic_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='pic_icon',
            field=models.ImageField(upload_to='rest_images/'),
        ),
    ]
