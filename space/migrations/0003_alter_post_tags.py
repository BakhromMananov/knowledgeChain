# Generated by Django 4.2.7 on 2024-05-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_userprofile_username_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='space.tag'),
        ),
    ]
