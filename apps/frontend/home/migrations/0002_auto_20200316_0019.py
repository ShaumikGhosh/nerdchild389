# Generated by Django 3.0.4 on 2020-03-16 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailfromvisitor',
            name='v_message',
        ),
        migrations.RemoveField(
            model_name='emailfromvisitor',
            name='v_subject',
        ),
        migrations.RemoveField(
            model_name='emailfromvisitor',
            name='v_user_name',
        ),
    ]
