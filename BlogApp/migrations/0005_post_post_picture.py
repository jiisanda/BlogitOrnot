# Generated by Django 4.0 on 2021-12-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_alter_post_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_picture',
            field=models.ImageField(blank=True, default='post_pictures\\Blog-It-Or-Not.png', null=True, upload_to='post_pictures'),
        ),
    ]