# Generated by Django 3.0.7 on 2020-10-22 15:09

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
# import inventory.models.kitchen


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20201022_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Kitchen name')),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Hidden'), (3, 'Available'), (4, 'Discontinued')], default=1, verbose_name='Status')),
                ('slug', models.SlugField(help_text='A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.', max_length=255, verbose_name='Slug')),
                ('search_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Search keywords')),
                ('description', models.TextField(verbose_name='Description')),
                ('can_be_painted', models.BooleanField(default=False, help_text='Designates whether the product can be painted in suppliers 2000 colors', verbose_name='Can be painted')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, default='media/products/default.jpg', null=True, upload_to='some/path/')),
                ('category', models.ManyToManyField(related_name='kitchens', to='inventory.SubCategory')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_kitchen', to='inventory.Supplier')),
            ],
        ),
    ]
