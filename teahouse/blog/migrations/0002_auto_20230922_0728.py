# Generated by Django 3.2.20 on 2023-09-22 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='replys',
        ),
        migrations.AddField(
            model_name='comment',
            name='replys',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogpost'),
        ),
    ]