# Generated by Django 5.1.5 on 2025-01-28 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_rename_data_added_topic_date_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
