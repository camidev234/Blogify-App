# Generated by Django 4.2.4 on 2023-10-11 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleManage', '0005_remove_userresponse_dislikes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='likes',
        ),
        migrations.AddField(
            model_name='userresponse',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
