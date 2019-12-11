# Generated by Django 2.1.7 on 2019-12-10 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bandeira', models.CharField(max_length=15)),
                ('numero', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=40)),
                ('telefone', models.CharField(max_length=16)),
                ('estado', models.CharField(choices=[('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'), ('Bahia ', 'BA'), ('Ceará', 'CE'), ('Distrito Federal ', 'DF'), ('Espírito Santo', 'ES'), ('Goiás', 'GO'), ('Maranhão', 'MA'), ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'), ('Minas Gerais', 'MG'), ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'), ('Pernambuco', 'PE'), ('Piauí', 'PI'), ('Rio de Janeiro', 'RJ'), ('Rio Grande do Norte', 'RN'), ('Rio Grande do Sul', 'RS'), ('Rondônia', 'RO'), ('Roraima', 'RR'), ('Santa Catarina', 'SC'), ('São Paulo', 'SP'), ('Sergipe', 'SE'), ('Tocantins', 'TO')], max_length=30)),
                ('cidade', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=80)),
                ('associados', models.IntegerField(blank=True, default=0)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('valor', models.FloatField()),
                ('incluso', models.TextField()),
                ('academia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planos', to='accounts.Gym')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('valor', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('descricao', models.TextField()),
                ('academia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='accounts.Gym')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=16)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=9)),
                ('nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=80)),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=9)),
                ('academias', models.ManyToManyField(blank=True, related_name='profiles', to='accounts.Gym')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('segunda_e', models.TimeField()),
                ('segunda_s', models.TimeField()),
                ('terca_e', models.TimeField()),
                ('terca_s', models.TimeField()),
                ('quarta_e', models.TimeField()),
                ('quarta_s', models.TimeField()),
                ('quinta_e', models.TimeField()),
                ('quinta_s', models.TimeField()),
                ('sexta_e', models.TimeField()),
                ('sexta_s', models.TimeField()),
                ('sabado_e', models.TimeField()),
                ('sabado_s', models.TimeField()),
                ('domingo_e', models.TimeField()),
                ('domingo_s', models.TimeField()),
                ('academia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='accounts.Gym')),
                ('planos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='accounts.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('contato', models.TextField()),
                ('academia', models.ManyToManyField(related_name='transportes', to='accounts.Gym')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='compradores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='plan',
            name='compradores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planos', to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='card',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartoes', to='accounts.Profile'),
        ),
    ]
