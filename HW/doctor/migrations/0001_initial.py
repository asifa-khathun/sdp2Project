# Generated by Django 3.2.3 on 2021-05-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demail', models.EmailField(max_length=254)),
                ('dname', models.CharField(max_length=100)),
                ('dage', models.CharField(max_length=3)),
                ('dgender', models.CharField(max_length=7)),
                ('dexperience', models.CharField(max_length=10)),
                ('dcontact', models.CharField(max_length=15)),
                ('dpsw', models.CharField(max_length=15)),
                ('donduty', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
    ]
