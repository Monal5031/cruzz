# Generated by Django 2.0.6 on 2018-11-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_auto_20181103_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover',
            field=models.URLField(blank=True, null=True),
        ),
    ]
