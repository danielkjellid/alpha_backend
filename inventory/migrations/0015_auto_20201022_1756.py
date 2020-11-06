# Generated by Django 3.0.7 on 2020-10-22 15:56

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import inventory.models.kitchen


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_kitchen'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenDecor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kitchen decor name')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=inventory.models.kitchen.KitchenDecor.kitchen_decor_directory_path)),
            ],
            options={
                'verbose_name': 'Kithcen decor',
                'verbose_name_plural': 'Kitchen decors',
            },
        ),
        migrations.CreateModel(
            name='KitchenExclusiveColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kitchen exclusive name')),
                ('color_hex', models.CharField(max_length=7, unique=True, verbose_name='Color code')),
            ],
            options={
                'verbose_name': 'Kithcen exclusive color',
                'verbose_name_plural': 'Kitchen exclusives colors',
            },
        ),
        migrations.CreateModel(
            name='KitchenLaminateColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kitchen laminate name')),
                ('color_hex', models.CharField(max_length=7, unique=True, verbose_name='Color code')),
            ],
            options={
                'verbose_name': 'Kithcen laminate color',
                'verbose_name_plural': 'Kitchen laminates colors',
            },
        ),
        migrations.CreateModel(
            name='KitchenPlywood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kitchen decor name')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=inventory.models.kitchen.KitchenPlywood.kitchen_plywood_directory_path)),
            ],
            options={
                'verbose_name': 'Kithcen decor',
                'verbose_name_plural': 'Kitchen decors',
            },
        ),
        migrations.CreateModel(
            name='KitchenSilkColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kitchen silk name')),
                ('color_hex', models.CharField(max_length=7, unique=True, verbose_name='Color code')),
            ],
            options={
                'verbose_name': 'Kithcen silk color',
                'verbose_name_plural': 'Kitchen silks colors',
            },
        ),
        migrations.CreateModel(
            name='KitchenTrendColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kitchen trend name')),
                ('color_hex', models.CharField(max_length=7, unique=True, verbose_name='Color code')),
            ],
            options={
                'verbose_name': 'Kithcen exclusive color',
                'verbose_name_plural': 'Kitchen exclusives colors',
            },
        ),
        migrations.AlterModelOptions(
            name='kitchen',
            options={'verbose_name': 'Kitchen', 'verbose_name_plural': 'Kitchens'},
        ),
        migrations.CreateModel(
            name='KitchenImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/kitchens/name/files/filename', verbose_name='Image')),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='inventory.Kitchen')),
            ],
            options={
                'verbose_name': 'Kitchen image',
                'verbose_name_plural': 'Kitchen images',
            },
        ),
        migrations.AddField(
            model_name='kitchen',
            name='decor_variants',
            field=models.ManyToManyField(blank=True, related_name='kitchen_decor', to='inventory.KitchenDecor'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='exclusive_variants',
            field=models.ManyToManyField(blank=True, related_name='kitchen_exclusive', to='inventory.KitchenExclusiveColor'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='laminate_variants',
            field=models.ManyToManyField(blank=True, related_name='kitchen_decor', to='inventory.KitchenLaminateColor'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='plywood_variants',
            field=models.ManyToManyField(blank=True, related_name='kitchen_plywood', to='inventory.KitchenPlywood'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='silk_variants',
            field=models.ManyToManyField(blank=True, related_name='kitchen_silk', to='inventory.KitchenSilkColor'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='trend_variants',
            field=models.ManyToManyField(blank=True, related_name='kitchen_decor', to='inventory.KitchenTrendColor'),
        ),
    ]