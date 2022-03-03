# Generated by Django 4.0.2 on 2022-02-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=125)),
                ('creator_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=125)),
                ('position', models.IntegerField()),
                ('slug', models.CharField(max_length=125)),
                ('start_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('cover_url', models.CharField(max_length=125)),
                ('card_list_id', models.BigIntegerField()),
                ('creator_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CardLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('card_id', models.BigIntegerField()),
                ('label_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CardList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=125)),
                ('position', models.IntegerField()),
                ('board_id', models.BigIntegerField()),
                ('creator_id', models.BigIntegerField()),
                ('sorted_by', models.CharField(max_length=50)),
                ('num_card_limit', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('card_id', models.BigIntegerField()),
                ('user_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('workspace_id', models.IntegerField()),
                ('creator_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkspaceMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('workspace_id', models.BigIntegerField()),
                ('user_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
