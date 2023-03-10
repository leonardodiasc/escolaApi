# Generated by Django 4.1.6 on 2023-02-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_alter_aluno_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='curso',
            name='codigo_curso',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado')], default='B', max_length=1),
        ),
    ]
