# Generated by Django 5.0.2 on 2024-02-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_alter_profile_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='auth_status',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_name',
            field=models.CharField(default='user', max_length=20),
        ),
    ]
