# Generated by Django 4.1.3 on 2022-11-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingmart', '0028_delete_adeemaform_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='adeemaform_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('age', models.CharField(default='', max_length=50)),
                ('father_name', models.CharField(default='', max_length=50)),
                ('datetime', models.DateTimeField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='student_data',
            name='Dath_Of_Birth',
        ),
    ]
