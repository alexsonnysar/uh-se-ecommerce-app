# Generated by Django 3.0.5 on 2020-04-22 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_item_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='picture',
        ),
    ]
