# Generated by Django 5.0.1 on 2024-01-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='url',
            field=models.CharField(default='None', max_length=256),
        ),
    ]
