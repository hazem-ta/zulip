# Generated by Django 1.11.6 on 2017-11-01 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0116_realm_allow_message_deleting"),
    ]

    operations = [
        migrations.AddField(
            model_name="usergroup",
            name="description",
            field=models.CharField(default="", max_length=1024),
        ),
    ]
