# Generated by Django 2.0.2 on 2018-02-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0011_auto_20180108_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
