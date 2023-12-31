# Generated by Django 4.2.3 on 2023-08-11 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_advertisement', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='Отметьте если торг возможен', verbose_name='Торг'),
        ),
    ]
