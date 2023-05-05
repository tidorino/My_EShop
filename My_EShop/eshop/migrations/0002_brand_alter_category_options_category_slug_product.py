# Generated by Django 4.2 on 2023-04-28 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/brand_img')),
                ('intro_text', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.PositiveIntegerField(default=0)),
                ('discounted_price', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='', max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/products')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.brand')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eshop.category')),
            ],
        ),
    ]