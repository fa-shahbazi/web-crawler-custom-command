# Generated by Django 3.2.6 on 2021-09-04 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is_enabled')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=130, verbose_name='name')),
                ('price', models.CharField(blank=True, max_length=50, verbose_name='price')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
    ]
