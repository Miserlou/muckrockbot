# Generated by Django 2.1.2 on 2019-01-05 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # ('feedreader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(blank=True, max_length=500)),
                ('entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='feedreader.Entry')),
            ],
        ),
    ]
