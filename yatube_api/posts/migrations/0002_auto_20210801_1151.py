# Generated by Django 2.2.6 on 2021-08-01 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
    ]