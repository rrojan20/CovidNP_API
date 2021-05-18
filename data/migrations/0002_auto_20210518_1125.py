# Generated by Django 3.2.3 on 2021-05-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='last24hours',
            options={'verbose_name_plural': 'Last 24 hours'},
        ),
        migrations.AddField(
            model_name='data',
            name='death_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='data',
            name='recovered_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
