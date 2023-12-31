# Generated by Django 4.2.5 on 2023-09-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_curso', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('qtt_modulos', models.PositiveIntegerField()),
                ('categoria', models.CharField(max_length=100)),
                ('avaliacao', models.DecimalField(decimal_places=2, max_digits=3)),
                ('instrutor', models.CharField(max_length=255)),
                ('plataforma', models.CharField(max_length=100)),
            ],
        ),
    ]
