# Generated by Django 2.2.9 on 2020-02-17 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('langauge_book', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'bebebe', 'verbose_name_plural': 'mememe'},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='catalog.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='languages', to='catalog.Language'),
        ),
    ]
