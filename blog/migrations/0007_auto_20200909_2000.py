# Generated by Django 2.2.5 on 2020-09-09 14:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_likes_jay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
