# Generated by Django 2.0.7 on 2022-06-28 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0012_auto_20220628_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercourse',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='uid',
        ),
        migrations.DeleteModel(
            name='userCourse',
        ),
    ]
