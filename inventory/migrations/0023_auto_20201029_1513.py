# Generated by Django 3.0.7 on 2020-10-29 14:13

from django.db import migrations, models
import imagekit.models.fields
import inventory.models.product


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_auto_20201029_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='media/products/default.jpg', help_text='Image must be above 380x575px', null=True, upload_to=inventory.models.product.Product.product_directory_path),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, help_text='Image must be above 3072x940px', null=True, upload_to=inventory.models.product.ProductImage.product_image_directory_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, help_text='Image must be above 380x575px', null=True, upload_to=inventory.models.product.ProductVariant.product_variant_directory_path),
        ),
    ]