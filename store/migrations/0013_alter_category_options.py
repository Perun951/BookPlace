# Generated by Django 4.1.6 on 2023-02-17 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name_plural': 'Categories'},
        ),
    ]
