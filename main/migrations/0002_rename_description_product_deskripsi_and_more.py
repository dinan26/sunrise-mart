# Generated by Django 5.1.1 on 2024-09-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='deskripsi',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='nama',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='harga',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
