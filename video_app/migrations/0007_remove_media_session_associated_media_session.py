# Generated by Django 5.0.6 on 2024-07-20 02:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("video_app", "0006_alter_media_session_associated"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="media",
            name="session_associated",
        ),
        migrations.AddField(
            model_name="media",
            name="session",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="video_app.session",
            ),
            preserve_default=False,
        ),
    ]