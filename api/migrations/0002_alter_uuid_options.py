# Generated by Django 4.0.1 on 2022-01-15 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uuid',
            options={'ordering': ['-id']},
        ),
    ]
