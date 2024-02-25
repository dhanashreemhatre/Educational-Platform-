# Generated by Django 4.1 on 2023-09-04 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eduapp", "0003_enrollment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enrollment",
            name="timestamp",
        ),
        migrations.AddField(
            model_name="enrollment",
            name="payment_status",
            field=models.CharField(default="fail", max_length=255),
        ),
    ]
