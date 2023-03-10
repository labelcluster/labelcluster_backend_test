# Generated by Django 4.1 on 2022-11-14 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gateway",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_id", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=20)),
                ("timestamp", models.DateTimeField()),
                ("sign", models.CharField(max_length=500)),
                ("sign_type", models.CharField(max_length=10)),
                ("encrypt_type", models.CharField(max_length=10)),
                ("biz_data", models.TextField()),
            ],
        ),
    ]
