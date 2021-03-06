# Generated by Django 3.0.7 on 2020-09-29 11:02

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
                ('slug', models.SlugField(help_text='A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.', verbose_name='Slug')),
                ('ordering', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Order  in which the category should be displayed.', verbose_name='Order')),
                ('width', models.CharField(blank=True, choices=[('full', 'Fullwidth'), ('half', 'Half')], default='full', max_length=4, null=True, verbose_name='Width')),
                ('image', models.ImageField(blank=True, help_text='Category image, should only be used on top level parents!', null=True, upload_to='media/categories', verbose_name='Image')),
                ('display_in_navbar', models.BooleanField(default=True, help_text='Designates whether the category should be displayed in the nav dropdown.', verbose_name='Display in navigation bar')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether the category should be treated as active.', verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Product name')),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Hidden'), (3, 'Available'), (4, 'Discontinued')], default=1, verbose_name='Status')),
                ('slug', models.SlugField(help_text='A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.', max_length=255, verbose_name='Slug')),
                ('short_description', models.TextField(help_text='The short description will be displayed on the top part of the product, above the variant selection', verbose_name='Short Description')),
                ('description', models.TextField(verbose_name='Description')),
                ('unit', models.IntegerField(choices=[(1, 'm2'), (2, 'stk')], default=1, verbose_name='Unit')),
                ('vat_rate', models.FloatField(default=0.25, verbose_name='VAT Rate')),
                ('gross_price', models.FloatField(verbose_name='Gross price')),
                ('available_in_special_sizes', models.BooleanField(default=False, help_text='Designates whether the product comes in sizes out of the ordinary', verbose_name='Available in special sizes')),
                ('absorption', models.FloatField(blank=True, null=True)),
                ('can_be_purchased_online', models.BooleanField(default=False, help_text='Designates whether the product can be purchased and shipped', verbose_name='Can be purchased online')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, default='media/products/default.jpg', null=True, upload_to='media/products')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product application',
                'verbose_name_plural': 'Product applications',
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('color_hex', models.CharField(max_length=7, unique=True, verbose_name='Color code')),
            ],
            options={
                'verbose_name': 'Product color',
                'verbose_name_plural': 'Product colors',
            },
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product material',
                'verbose_name_plural': 'Product materials',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField(help_text='width in centimeters', verbose_name='Width')),
                ('height', models.IntegerField(help_text='height in centimeters', verbose_name='Height')),
                ('depth', models.IntegerField(blank=True, help_text='depth in centimeters', null=True, verbose_name='Depth')),
            ],
            options={
                'verbose_name': 'Product size',
                'verbose_name_plural': 'Product sizes',
            },
        ),
        migrations.CreateModel(
            name='ProductStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product style',
                'verbose_name_plural': 'Product styles',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Supplier name')),
                ('contact_first_name', models.CharField(max_length=255, verbose_name='Contact first name')),
                ('contact_last_name', models.CharField(max_length=255, verbose_name='Contact last name')),
                ('contact_email', models.EmailField(max_length=254, unique=True, verbose_name='Contact email address')),
                ('origin_country', models.CharField(max_length=255, verbose_name='Origin country')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether the category should be treated as active.', verbose_name='Active')),
            ],
            options={
                'verbose_name': 'supplier',
                'verbose_name_plural': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
                ('slug', models.SlugField(help_text='A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.', verbose_name='Slug')),
                ('ordering', models.PositiveSmallIntegerField(blank=True, default=0, help_text='Order  in which the category should be displayed.', verbose_name='Order')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether the category should be treated as active.', verbose_name='Active')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='inventory.Category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Product variant name')),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Hidden'), (3, 'Available'), (4, 'Discontinued')], default=1, verbose_name='Status')),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='media/products/variants')),
                ('additional_cost', models.FloatField(verbose_name='Additional cost')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='inventory.Product')),
            ],
            options={
                'verbose_name': 'Product variant',
                'verbose_name_plural': 'Product variants',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='inventory.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='applications',
            field=models.ManyToManyField(related_name='product_application', to='inventory.ProductApplication'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='inventory.SubCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(related_name='product_color', to='inventory.ProductColor'),
        ),
        migrations.AddField(
            model_name='product',
            name='materials',
            field=models.ManyToManyField(related_name='product_material', to='inventory.ProductMaterial'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(related_name='product_size', to='inventory.ProductSize'),
        ),
        migrations.AddField(
            model_name='product',
            name='styles',
            field=models.ManyToManyField(related_name='product_style', to='inventory.ProductStyle'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_product', to='inventory.Supplier'),
        ),
    ]
