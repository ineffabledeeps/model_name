# Generated by Django 4.0.6 on 2022-08-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_name', '0013_faculties_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculties',
            name='available',
            field=models.BooleanField(default=False, max_length=100),
        ),
    ]
