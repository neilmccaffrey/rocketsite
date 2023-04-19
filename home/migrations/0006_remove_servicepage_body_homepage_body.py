# Generated by Django 4.1.7 on 2023-04-10 23:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_servicepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', required=True))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
