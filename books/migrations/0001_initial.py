# Generated by Django 4.2.6 on 2023-10-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('author', models.CharField(max_length=127)),
                ('cover', models.CharField(choices=[('Hard', 'Hard'), ('Soft', 'Soft')], default='Hard', max_length=4)),
                ('inventory', models.IntegerField()),
                ('daily_fee', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
