# Generated by Django 3.0.3 on 2025-01-03 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemshots',
            old_name='movie',
            new_name='item',
        ),
    ]
