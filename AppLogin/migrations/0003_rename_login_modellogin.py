# Generated by Django 4.1 on 2022-09-18 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppLogin', '0002_rename_user_login_useremail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='ModelLogin',
        ),
    ]