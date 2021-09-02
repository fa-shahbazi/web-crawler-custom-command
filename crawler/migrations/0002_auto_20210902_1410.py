# Generated by Django 3.2.6 on 2021-09-02 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='is_enabled',
            field=models.BooleanField(default=True, verbose_name='is_enabled'),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='updated time'),
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
