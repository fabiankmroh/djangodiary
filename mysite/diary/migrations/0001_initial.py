# Generated by Django 2.1.1 on 2019-07-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date written')),
            ],
        ),
    ]
