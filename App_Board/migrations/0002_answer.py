# Generated by Django 3.2.8 on 2021-10-30 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_data', models.DateTimeField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Board.question')),
            ],
        ),
    ]