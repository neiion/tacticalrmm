# Generated by Django 2.2.4 on 2019-09-16 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='uninstall_pending',
            field=models.BooleanField(default=False),
        ),
    ]