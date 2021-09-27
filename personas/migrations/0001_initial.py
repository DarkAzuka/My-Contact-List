# Generated by Django 3.2.6 on 2021-08-25 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('pais', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=255)),
                ('numero_ext', models.CharField(max_length=25)),
                ('numero_int', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casado', models.CharField(choices=[('No', 'Soltero'), ('Si', 'Casado')], default='No', max_length=2)),
                ('trabajo', models.CharField(choices=[('Si', 'Si Trabajo'), ('No', 'No Trabajo')], default='Si', max_length=2)),
                ('sociales', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('nombres', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('email', models.CharField(max_length=255)),
                ('domicilio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.domicilio')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('fecha_registro', models.DateField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('info_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.ocupacion')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.persona')),
            ],
        ),
    ]
