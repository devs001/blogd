# Generated by Django 3.0.7 on 2020-09-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website_link',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
