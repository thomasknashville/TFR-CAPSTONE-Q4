# Generated by Django 3.2.5 on 2021-07-13 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0005_alter_restaurant_pic_icon'),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rest_match', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
