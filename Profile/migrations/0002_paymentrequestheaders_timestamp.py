# Generated by Django 2.2.6 on 2019-10-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrequestheaders',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
