# Generated by Django 4.2.13 on 2024-05-23 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_proj_cert_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proj_cert',
            old_name='url',
            new_name='Proj_Cert_url',
        ),
    ]
