# Generated by Django 4.1.3 on 2022-11-14 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingmart', '0005_rename_fathername_student_data_father_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_data',
            old_name='Username',
            new_name='User_name',
        ),
    ]
