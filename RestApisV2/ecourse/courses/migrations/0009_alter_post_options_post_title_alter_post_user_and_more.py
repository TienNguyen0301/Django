# Generated by Django 4.0.3 on 2022-04-13 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.CreateModel(
            name='Imagepost',
            fields=[
                ('image_post_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(db_collation='utf8_general_ci', max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageposts', to='courses.post')),
            ],
            options={
                'db_table': 'imagepost',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('auction_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField()),
                ('price', models.BigIntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='courses.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Liked',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='courses.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'liked',
                'managed': True,
                'unique_together': {('post', 'user')},
            },
        ),
    ]
