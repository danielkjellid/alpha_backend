# Generated by Django 3.0.7 on 2020-10-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20201001_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='contact_email',
            field=models.EmailField(max_length=254, verbose_name='Contact email address'),
        ),
    ]