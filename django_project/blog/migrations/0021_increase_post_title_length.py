# Generated by Django 4.0.6 on 2022-07-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0020_changed_metaimg_alt_text_length"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
