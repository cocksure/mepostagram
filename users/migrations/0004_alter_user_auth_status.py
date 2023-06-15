# Generated by Django 4.2.1 on 2023-05-18 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userconfirmation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='auth_status',
            field=models.CharField(choices=[('new', 'new'), ('code_verified', 'code_verified'), ('done', 'done'), ('photo_step', 'photo_step')], default='new', max_length=31),
        ),
    ]