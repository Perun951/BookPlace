# Generated by Django 4.1.6 on 2023-02-24 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_author_alter_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
