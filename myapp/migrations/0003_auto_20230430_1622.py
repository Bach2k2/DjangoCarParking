# Generated by Django 3.2.18 on 2023-04-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_user_is_cashier'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_customer', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False),
        ),
    ]
