# Generated by Django 4.2.4 on 2023-10-11 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ArticleManage', '0007_remove_userresponse_dislikes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArticleManage.userresponse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'response')},
            },
        ),
        migrations.AddField(
            model_name='userresponse',
            name='dislikes',
            field=models.ManyToManyField(related_name='disliked_responses', through='ArticleManage.Dislike', to=settings.AUTH_USER_MODEL),
        ),
    ]
