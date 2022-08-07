# Generated by Django 4.0.6 on 2022-07-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_name', '0010_alter_meeting_req_request_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='classroom',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='course',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dept',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='faculties',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='meeting_req',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='students',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]