# Generated by Django 3.2.21 on 2023-09-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_exceldemo_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exceldemo',
            name='number',
            field=models.IntegerField(),
        ),
    ]
