# Generated by Django 4.2.7 on 2024-03-29 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="financetransaction",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
