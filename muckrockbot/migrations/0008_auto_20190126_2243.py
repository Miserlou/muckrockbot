# Generated by Django 2.1.2 on 2019-01-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muckrockbot', '0007_auto_20190126_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='tweet_id',
        ),
        migrations.AddField(
            model_name='request',
            name='completed_tweet_id',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='request',
            name='submitted_tweet_id',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]