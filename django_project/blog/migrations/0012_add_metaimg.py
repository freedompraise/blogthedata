# Generated by Django 3.2.7 on 2022-03-25 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_add_draft_post_boolean"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="metaimg",
            field=models.ImageField(default="jsolly.jpeg", upload_to="post_metaimgs/"),
        ),
        migrations.AddField(
            model_name="post",
            name="metaimg_mimetype",
            field=models.CharField(default="image/jpeg", max_length=20),
        ),
    ]
