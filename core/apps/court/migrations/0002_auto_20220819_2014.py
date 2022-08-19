# Generated by Django 3.1.7 on 2022-08-19 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establishment', '0001_initial'),
        ('court', '0001_initial'),
        ('sport', '0002_auto_20220819_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='establishmet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishment.establishment'),
        ),
        migrations.AddField(
            model_name='court',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.sport'),
        ),
    ]