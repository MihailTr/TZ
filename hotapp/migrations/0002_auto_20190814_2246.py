# Generated by Django 2.2.4 on 2019-08-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
