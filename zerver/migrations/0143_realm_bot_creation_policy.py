# Generated by Django 1.11.6 on 2018-03-09 18:00
from django.db import migrations, models
from django.db.backends.postgresql.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps

BOT_CREATION_EVERYONE = 1


def set_initial_value_for_bot_creation_policy(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    Realm = apps.get_model("zerver", "Realm")
    Realm.BOT_CREATION_EVERYONE = 1
    Realm.BOT_CREATION_LIMIT_GENERIC_BOTS = 2
    for realm in Realm.objects.all():
        if realm.create_generic_bot_by_admins_only:
            realm.bot_creation_policy = Realm.BOT_CREATION_LIMIT_GENERIC_BOTS
        else:
            realm.bot_creation_policy = Realm.BOT_CREATION_EVERYONE
        realm.save(update_fields=["bot_creation_policy"])


def reverse_code(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    Realm = apps.get_model("zerver", "Realm")
    Realm.BOT_CREATION_EVERYONE = 1
    for realm in Realm.objects.all():
        if realm.bot_creation_policy == Realm.BOT_CREATION_EVERYONE:
            realm.create_generic_bot_by_admins_only = False
        else:
            realm.create_generic_bot_by_admins_only = True
        realm.save(update_fields=["create_generic_bot_by_admins_only"])


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0142_userprofile_translate_emoticons"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="bot_creation_policy",
            field=models.PositiveSmallIntegerField(default=BOT_CREATION_EVERYONE),
        ),
        migrations.RunPython(
            set_initial_value_for_bot_creation_policy, reverse_code=reverse_code, elidable=True
        ),
    ]
