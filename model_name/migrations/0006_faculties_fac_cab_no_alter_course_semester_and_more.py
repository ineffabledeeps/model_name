# Generated by Django 4.0.6 on 2022-07-27 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_name', '0005_sem'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculties',
            name='fac_cab_no',
            field=models.IntegerField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_name.students'),
        ),
        migrations.AlterField(
            model_name='students',
            name='dept_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_name.dept'),
        ),
    ]