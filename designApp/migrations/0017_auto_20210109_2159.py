# Generated by Django 3.0.8 on 2021-01-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designApp', '0016_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='system_image1',
            field=models.ImageField(upload_to='systems/'),
        ),
        migrations.AlterField(
            model_name='system',
            name='system_image2',
            field=models.ImageField(upload_to='systems/'),
        ),
    ]
