# Generated by Django 4.0.3 on 2022-04-16 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_tag_action_active_comment_active_rating_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='courses.tag'),
        ),
    ]