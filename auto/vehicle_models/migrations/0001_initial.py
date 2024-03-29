# Generated by Django 3.0.4 on 2020-07-12 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandName', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelName', models.CharField(blank=True, max_length=60, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_models.VehicleBrand')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleSubModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subModel', models.CharField(blank=True, max_length=60, null=True)),
                ('parentModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_models.VehicleModel')),
            ],
        ),
    ]
