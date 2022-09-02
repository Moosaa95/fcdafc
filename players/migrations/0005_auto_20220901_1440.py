# Generated by Django 3.1.7 on 2022-09-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20220901_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerinfo',
            name='words',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='playerinfo',
            name='bio',
            field=models.TextField(max_length=300),
        ),
    ]