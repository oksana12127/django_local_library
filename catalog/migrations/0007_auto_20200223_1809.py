# Generated by Django 2.2.9 on 2020-02-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200223_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datewriting',
            name='date_book',
            field=models.CharField(max_length=100),
        ),
    ]
