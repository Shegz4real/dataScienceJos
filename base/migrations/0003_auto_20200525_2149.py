# Generated by Django 2.2.6 on 2020-05-25 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_newmember_usersurname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newmember',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='newmember',
            old_name='username',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='newmember',
            old_name='usersurname',
            new_name='surname',
        ),
    ]
