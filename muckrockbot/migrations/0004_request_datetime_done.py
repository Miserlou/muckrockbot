# Generated by Django 2.1.2 on 2019-01-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muckrockbot', '0003_auto_20190119_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='datetime_done',
            field=models.DateTimeField(null=True),
        ),
    ]