# Generated by Django 2.0 on 2020-06-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character_role',
            name='character_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]