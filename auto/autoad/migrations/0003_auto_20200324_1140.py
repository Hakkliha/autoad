# Generated by Django 3.0.4 on 2020-03-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoad', '0002_auto_20200324_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='displacement_cm',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='power_kw',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]