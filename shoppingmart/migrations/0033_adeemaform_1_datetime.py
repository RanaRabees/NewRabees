# Generated by Django 4.1.3 on 2022-11-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingmart', '0032_remove_adeemaform_1_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='adeemaform_1',
            name='datetime',
            field=models.DateTimeField(default=''),
        ),
    ]
