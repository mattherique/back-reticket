# Generated by Django 5.2.1 on 2025-05-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pass_hash', models.CharField(max_length=256)),
                ('sal', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=32)),
                ('location', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'db_users',
            },
        ),
    ]
