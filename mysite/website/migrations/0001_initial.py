# Generated by Django 4.2.3 on 2023-08-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stduent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('collage', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=10)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
