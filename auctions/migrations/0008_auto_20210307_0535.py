# Generated by Django 3.1.7 on 2021-03-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210307_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
