# Generated by Django 2.2.5 on 2020-09-11 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='jay_user',
            name='bio',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
