# Generated by Django 3.1.1 on 2020-09-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0004_auto_20200906_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_qty',
            field=models.IntegerField(default='1', max_length=4),
        ),
    ]
