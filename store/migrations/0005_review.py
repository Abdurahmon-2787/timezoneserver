# Generated by Django 4.2.3 on 2023-07-25 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_alter_product_colour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Izoh')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='izoh qoldirilgan')),
                ('publish', models.BooleanField(default=True, verbose_name='Chop etish')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='avtor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Izoh',
                'verbose_name_plural': 'Izohlar',
            },
        ),
    ]
