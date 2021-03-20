# Generated by Django 3.0.7 on 2021-03-18 18:35

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('inventory', '0035_auto_20210206_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': (('has_products_list', 'Can list products'), ('has_product_edit', 'Can edit a single product instance'), ('has_product_add', 'Can add a single product instance'), ('has_product_delete', 'Can delete a single product instance')), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='can_be_picked_up',
            field=models.BooleanField(default=False, help_text='Designates whether the product can be purchased and picked up in store', verbose_name='Can be picked up'),
        ),
        migrations.AddField(
            model_name='product',
            name='sites',
            field=models.ManyToManyField(related_name='product_site', to='sites.Site'),
        ),
    ]