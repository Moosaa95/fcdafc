# Generated by Django 3.1.7 on 2022-09-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_playerinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerinfo',
            name='height',
            field=models.CharField(default='cm', max_length=30),
        ),
        migrations.AlterField(
            model_name='playerinfo',
            name='states',
            field=models.CharField(choices=[('Adamawa', 'Adamawa'), ('AkwaIbom', 'AkwaIbom'), ('Abia', 'Abia'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('CrossRiver', 'CrossRiver'), ('Delta', 'Delta'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Ebonyi', 'Ebonyi'), ('FCT', 'FCT'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kano', 'Kano'), ('Kaduna', 'Kaduna'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], max_length=50),
        ),
        migrations.AlterField(
            model_name='playerinfo',
            name='weight',
            field=models.CharField(default='kg', max_length=20),
        ),
    ]
