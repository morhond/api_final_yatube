# Generated by Django 3.2.3 on 2022-11-24 12:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_auto_20221124_1507'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'following')},
        ),
    ]
