# Generated by Django 2.1.7 on 2019-10-02 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('cpf', models.CharField(max_length=100, verbose_name='CPF Number')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('number', models.CharField(max_length=100, verbose_name='Passport Number')),
                ('issue_date', models.DateField(verbose_name='Issue Date')),
                ('expiration_date', models.DateField(verbose_name='Expiration Date')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exemplo.Person')),
            ],
        ),
    ]
