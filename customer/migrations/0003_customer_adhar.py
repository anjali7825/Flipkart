# Generated by Django 4.2.1 on 2023-05-27 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Adhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_name', models.CharField(blank=True, max_length=15, null=True)),
                ('adhar_no', models.IntegerField(blank=True, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
