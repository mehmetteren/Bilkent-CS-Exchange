# Generated by Django 4.1.3 on 2022-12-15 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileAnalyzeApp', '0002_alter_excelstudents_studentid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='excelstudents',
            old_name='Lastname',
            new_name='lastname',
        ),
    ]
