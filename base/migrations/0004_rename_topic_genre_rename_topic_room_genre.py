# Generated by Django 4.2 on 2023-05-10 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room_host'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Genre',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='topic',
            new_name='genre',
        ),
    ]
