# Generated by Django 4.0.6 on 2022-07-30 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_name', '0009_remove_meeting_req_id_alter_meeting_req_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting_req',
            name='request_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
