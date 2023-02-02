# Generated by Django 3.2.5 on 2021-07-09 11:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0330_linkifier_pattern_validator"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScheduledMessageNotificationEmail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "trigger",
                    models.TextField(
                        choices=[
                            ("private_message", "Private message"),
                            ("mentioned", "Mention"),
                            ("wildcard_mentioned", "Wildcard mention"),
                            ("stream_email_notify", "Stream notifications enabled"),
                        ]
                    ),
                ),
                ("scheduled_timestamp", models.DateTimeField(db_index=True)),
                (
                    "mentioned_user_group",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="zerver.usergroup",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zerver.message"
                    ),
                ),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
