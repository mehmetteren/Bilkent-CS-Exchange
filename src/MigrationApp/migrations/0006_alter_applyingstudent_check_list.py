# Generated by Django 4.0 on 2022-11-20 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MigrationApp', '0005_alter_applyingstudent_check_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyingstudent',
            name='check_list',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='MigrationApp.todolist'),
        ),
    ]
