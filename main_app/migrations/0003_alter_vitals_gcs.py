# Generated by Django 3.2.7 on 2021-11-30 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20211129_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitals',
            name='gcs',
            field=models.IntegerField(default=15, verbose_name='Glasgow Coma Scale'),
        ),
    ]