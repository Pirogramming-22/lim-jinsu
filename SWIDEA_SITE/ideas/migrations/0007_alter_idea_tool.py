# Generated by Django 5.1.5 on 2025-01-15 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_alter_idea_tool'),
        ('tools', '0003_remove_tool_icon_alter_tool_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tools.tool'),
        ),
    ]
