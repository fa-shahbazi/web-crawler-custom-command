# Generated by Django 3.2.6 on 2021-09-11 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_phoneotp_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhoneOTP',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
