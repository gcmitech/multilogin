# Generated by Django 4.0.8 on 2022-11-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_binmanageruser_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='token',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
