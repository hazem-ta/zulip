# Generated by Django 1.11.14 on 2018-09-25 12:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0014_cleanup_pushdevicetoken"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="billingprocessor",
            name="log_row",
        ),
        migrations.RemoveField(
            model_name="billingprocessor",
            name="realm",
        ),
        migrations.DeleteModel(
            name="Coupon",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="realm",
        ),
        migrations.DeleteModel(
            name="Plan",
        ),
        migrations.DeleteModel(
            name="BillingProcessor",
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
    ]
