# Generated by Django 3.1.2 on 2020-11-26 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_productinbasket_session_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinbasket',
            old_name='count',
            new_name='nmb',
        ),
    ]
