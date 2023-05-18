# Generated by Django 3.2.18 on 2023-05-02 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20230502_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=20, unique=True)),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('car_model', models.CharField(max_length=100)),
                ('car_color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=20)),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('total_cost', models.IntegerField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.car')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.IntegerField(unique=True)),
                ('parking_type', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('is_available', models.BooleanField(default=True)),
                ('cost_per_day', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ParkingLot',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='car_color',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='car_model',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cost_per_day',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='days_spent',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='device',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='exit_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_payed',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='total_cost',
        ),
        migrations.AddField(
            model_name='parkingrecord',
            name='parking_slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.parkingslot'),
        ),
    ]