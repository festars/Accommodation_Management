# Generated by Django 2.2.6 on 2019-10-31 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_auto_20191031_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomateselection',
            name='user_roomate',
            field=models.CharField(max_length=191),
        ),
    ]
