# Generated by Django 4.1.5 on 2023-02-05 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0005_mailing_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mails.version'),
        ),
    ]