# Generated by Django 5.0.6 on 2024-06-23 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logining', '0003_alter_client_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logining.user', unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
