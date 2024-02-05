# Generated by Django 5.0.1 on 2024-02-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_profile_auth_status_profile_wrong_password_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avarar',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='wrong_password_count',
        ),
        migrations.AddField(
            model_name='profile',
            name='selected_option',
            field=models.IntegerField(choices=[(0, '😎'), (1, '🤩'), (3, '😇'), (4, '🥸')], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='color',
            field=models.IntegerField(default=0),
        ),
    ]