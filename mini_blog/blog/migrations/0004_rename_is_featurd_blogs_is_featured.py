# Generated by Django 5.1.2 on 2024-10-26 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogs_options_alter_blogs_staus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='is_featurd',
            new_name='is_featured',
        ),
    ]
