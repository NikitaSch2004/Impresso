# Generated by Django 4.2.5 on 2025-02-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Impresso', '0002_reservation_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('bon', models.IntegerField()),
                ('prize', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
