# Generated by Django 4.0.3 on 2022-05-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_rename_stock_id_item_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(blank=True, to='items.itemcategory'),
        ),
    ]
