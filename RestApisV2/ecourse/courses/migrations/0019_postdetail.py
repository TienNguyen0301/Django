# Generated by Django 4.0.3 on 2022-04-17 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_rename_creator_comment_user_alter_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default=None, upload_to='users/%Y/%m')),
                ('content', models.TextField(blank=True, null=True)),
                ('auctioneer', models.CharField(max_length=1)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postdetail', to='courses.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]