# Generated by Django 4.2.3 on 2023-08-08 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=55)),
                ('empId', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('working', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=10)),
            ],
        ),
    ]