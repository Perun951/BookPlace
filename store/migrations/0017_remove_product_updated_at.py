# Generated by Django 4.1.6 on 2023-02-19 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_product_editie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
    ]
