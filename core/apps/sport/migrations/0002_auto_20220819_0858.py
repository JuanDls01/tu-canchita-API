# Generated by Django 3.1.7 on 2022-08-19 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Sport',
        ),
        migrations.AlterModelOptions(
            name='sport',
            options={'verbose_name': 'Sport', 'verbose_name_plural': 'Sports'},
        ),
    ]
