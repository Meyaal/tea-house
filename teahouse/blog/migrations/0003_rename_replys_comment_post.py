# Generated by Django 3.2.20 on 2023-09-22 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230922_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='replys',
            new_name='post',
        ),
    ]
