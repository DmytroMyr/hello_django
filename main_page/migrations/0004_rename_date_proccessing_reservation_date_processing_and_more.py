# Generated by Django 4.1.6 on 2023-02-11 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_rename_date_priccessing_reservation_date_proccessing_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='date_proccessing',
            new_name='date_processing',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='is_proccessed',
            new_name='is_processed',
        ),
    ]
