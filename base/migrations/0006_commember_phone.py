# Generated by Django 2.2.6 on 2020-05-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20200526_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='commember',
            name='phone',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
    ]
