# Generated by Django 3.0.8 on 2020-08-17 14:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20200817_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-datetime', 'title']},
        ),
    ]
