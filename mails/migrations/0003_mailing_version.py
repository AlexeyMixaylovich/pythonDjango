# Generated by Django 4.1.5 on 2023-02-05 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0002_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mails.version'),
        ),
    ]