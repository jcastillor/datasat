# Generated by Django 3.0.2 on 2020-02-10 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='satelite2',
            name='type',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]