# Generated by Django 3.0.8 on 2020-07-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200719_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='discount',
            field=models.IntegerField(null=True),
        ),
    ]
