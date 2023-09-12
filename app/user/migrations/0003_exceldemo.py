# Generated by Django 3.2.21 on 2023-09-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_demo_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=12)),
                ('country_code', models.CharField(default='91', max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
