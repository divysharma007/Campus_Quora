# Generated by Django 3.1 on 2021-01-22 20:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainContent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=ckeditor.fields.RichTextField(default='nothing', max_length=5000),
        ),
    ]