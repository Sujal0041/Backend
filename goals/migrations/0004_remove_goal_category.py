# Generated by Django 4.2.7 on 2024-04-22 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("goals", "0003_goal_category_goal_wallet"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="goal",
            name="category",
        ),
    ]
