# Generated by Django 2.2.6 on 2021-08-02 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date']},
        ),
    ]
