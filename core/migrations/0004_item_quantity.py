# Generated by Django 3.0.5 on 2020-04-19 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_item_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="item", name="quantity", field=models.IntegerField(default=1),
        ),
    ]
