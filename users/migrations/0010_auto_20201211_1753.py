# Generated by Django 3.0.7 on 2020-12-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201211_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlastsession',
            name='status',
            field=models.IntegerField(choices=[(1, 'onLine'), (2, 'offLine')], default=1, max_length=200),
        ),
    ]
