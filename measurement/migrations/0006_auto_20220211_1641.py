# Generated by Django 3.1.2 on 2022-02-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_auto_20220211_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]