# Generated by Django 4.0.3 on 2022-06-14 18:09

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=users.models.Role.get_default_pk, on_delete=django.db.models.deletion.PROTECT, to='users.role'),
        ),
    ]
