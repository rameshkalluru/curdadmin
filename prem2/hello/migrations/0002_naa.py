# Generated by Django 4.0.2 on 2022-02-24 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='naa',
            fields=[
                ('nav_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hello.nav')),
                ('empno', models.IntegerField()),
            ],
            bases=('hello.nav',),
        ),
    ]