# Generated by Django 3.0.4 on 2020-03-17 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailfromvisitor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='EmailFromVisitor',
        ),
    ]