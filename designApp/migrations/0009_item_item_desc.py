# Generated by Django 3.0.8 on 2021-01-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designApp', '0008_auto_20210104_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_desc',
            field=models.CharField(default='', max_length=200),
        ),
    ]
