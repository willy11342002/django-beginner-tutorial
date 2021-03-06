# Generated by Django 3.2.12 on 2022-03-17 04:07

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProxy',
            fields=[
            ],
            options={
                'verbose_name': 'staff',
                'verbose_name_plural': 'staff',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.user',),
            managers=[
                ('objects', user.models.StaffManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProxy',
            fields=[
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.user',),
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'group', 'verbose_name_plural': 'group'},
        ),
    ]
