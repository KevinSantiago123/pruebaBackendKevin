# Generated by Django 2.2 on 2019-04-29 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ('nombre',)},
        ),
    ]
