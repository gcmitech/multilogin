# Generated by Django 4.0.8 on 2022-11-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_smartcontroluser_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinManagerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Username')),
                ('password', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=32, null=True)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('department_id', models.IntegerField()),
                ('position', models.IntegerField()),
                ('is_root', models.IntegerField()),
                ('is_firstuse', models.IntegerField()),
                ('is_active', models.IntegerField()),
            ],
        ),
    ]