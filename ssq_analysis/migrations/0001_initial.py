# Generated by Django 2.0.6 on 2018-06-26 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SsqInfo',
            fields=[
                ('number', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('red01', models.PositiveIntegerField()),
                ('red02', models.PositiveIntegerField()),
                ('red03', models.PositiveIntegerField()),
                ('red04', models.PositiveIntegerField()),
                ('red05', models.PositiveIntegerField()),
                ('red06', models.PositiveIntegerField()),
                ('red07', models.PositiveIntegerField()),
                ('red08', models.PositiveIntegerField()),
                ('red09', models.PositiveIntegerField()),
                ('red10', models.PositiveIntegerField()),
                ('red11', models.PositiveIntegerField()),
                ('red12', models.PositiveIntegerField()),
                ('red13', models.PositiveIntegerField()),
                ('red14', models.PositiveIntegerField()),
                ('red15', models.PositiveIntegerField()),
                ('red16', models.PositiveIntegerField()),
                ('red17', models.PositiveIntegerField()),
                ('red18', models.PositiveIntegerField()),
                ('red19', models.PositiveIntegerField()),
                ('red20', models.PositiveIntegerField()),
                ('red21', models.PositiveIntegerField()),
                ('red22', models.PositiveIntegerField()),
                ('red23', models.PositiveIntegerField()),
                ('red24', models.PositiveIntegerField()),
                ('red25', models.PositiveIntegerField()),
                ('red26', models.PositiveIntegerField()),
                ('red27', models.PositiveIntegerField()),
                ('red28', models.PositiveIntegerField()),
                ('red29', models.PositiveIntegerField()),
                ('red30', models.PositiveIntegerField()),
                ('red31', models.PositiveIntegerField()),
                ('red32', models.PositiveIntegerField()),
                ('red33', models.PositiveIntegerField()),
                ('blue01', models.PositiveIntegerField()),
                ('blue02', models.PositiveIntegerField()),
                ('blue03', models.PositiveIntegerField()),
                ('blue04', models.PositiveIntegerField()),
                ('blue05', models.PositiveIntegerField()),
                ('blue06', models.PositiveIntegerField()),
                ('blue07', models.PositiveIntegerField()),
                ('blue08', models.PositiveIntegerField()),
                ('blue09', models.PositiveIntegerField()),
                ('blue10', models.PositiveIntegerField()),
                ('blue11', models.PositiveIntegerField()),
                ('blue12', models.PositiveIntegerField()),
                ('blue13', models.PositiveIntegerField()),
                ('blue14', models.PositiveIntegerField()),
                ('blue15', models.PositiveIntegerField()),
                ('blue16', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SsqNum',
            fields=[
                ('number', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('red1', models.CharField(max_length=2)),
                ('red2', models.CharField(max_length=2)),
                ('red3', models.CharField(max_length=2)),
                ('red4', models.CharField(max_length=2)),
                ('red5', models.CharField(max_length=2)),
                ('red6', models.CharField(max_length=2)),
                ('blue', models.CharField(max_length=2)),
            ],
        ),
    ]