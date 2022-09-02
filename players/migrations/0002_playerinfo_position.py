# Generated by Django 3.1.7 on 2022-08-27 18:46

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerinfo',
            name='position',
            field=models.CharField(choices=[('STRIKER', 'STRIKER'), ('MIDFIELD', 'MIDFIELD'), ('DEFENDER', 'DEFENDER'), ('GOALKEEPER', 'GOALKEEPER')], default=builtins.dir, max_length=10),
            preserve_default=False,
        ),
    ]
