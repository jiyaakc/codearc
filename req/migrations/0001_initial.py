# Generated by Django 3.2.25 on 2025-02-09 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepairRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('model_number', models.CharField(blank=True, max_length=50, null=True)),
                ('problem_description', models.TextField()),
                ('photo', models.ImageField(upload_to='repair_photos/')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
