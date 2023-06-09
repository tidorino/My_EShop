# Generated by Django 4.2.1 on 2023-05-10 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0008_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='category_slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
