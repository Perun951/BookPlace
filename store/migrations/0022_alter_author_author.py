# Generated by Django 4.1.6 on 2023-02-19 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_author_author_author_slug_alter_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author',
            field=models.TextField(max_length=50),
        ),
    ]
