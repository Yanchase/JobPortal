# Generated by Django 4.2.10 on 2024-03-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
