# Generated by Django 4.0.6 on 2022-08-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_student_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_otp',
            name='user',
        ),
        migrations.AddField(
            model_name='user_otp',
            name='user_email',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
