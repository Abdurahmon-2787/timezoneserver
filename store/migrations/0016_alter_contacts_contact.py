# Generated by Django 4.2.3 on 2023-08-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_contacts_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
