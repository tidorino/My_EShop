# Generated by Django 4.2.1 on 2023-05-11 08:14

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0009_rename_slug_category_category_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeManyToManyField(to='eshop.category'),
        ),
    ]