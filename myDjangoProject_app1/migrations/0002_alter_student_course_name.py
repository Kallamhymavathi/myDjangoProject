# Generated by Django 5.1.2 on 2024-10-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDjangoProject_app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_name',
            field=models.CharField(default='Django', max_length=50),
        ),
    ]
