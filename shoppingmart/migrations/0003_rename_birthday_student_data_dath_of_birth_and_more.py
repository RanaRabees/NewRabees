# Generated by Django 4.1.3 on 2022-11-14 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingmart', '0002_student_data_delete_shoppify'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_data',
            old_name='Birthday',
            new_name='Dath_Of_Birth',
        ),
        migrations.RenameField(
            model_name='student_data',
            old_name='Area',
            new_name='Email',
        ),
    ]
