# Generated by Django 3.0.8 on 2020-07-17 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('can_manage_customers', 'Customer CRUD Operations'),)},
        ),
    ]
