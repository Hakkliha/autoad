# Generated by Django 3.0.4 on 2020-03-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoad', '0012_auto_20200326_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='autoad/media/%Y/%m/%d'),
        ),
    ]
