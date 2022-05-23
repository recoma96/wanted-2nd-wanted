# Generated by Django 4.0.4 on 2022-05-23 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='회사 생성한 사람')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='CompanyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'db_table': 'company_name',
            },
        ),
        migrations.CreateModel(
            name='CompanyTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'db_table': 'company_tag',
            },
        ),
        migrations.CreateModel(
            name='CompanyNameLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=10)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companyname')),
            ],
            options={
                'db_table': 'company_name_language',
            },
        ),
        migrations.CreateModel(
            name='CompanyContents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(default='', verbose_name='소개글')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'db_table': 'company_contents',
            },
        ),
        migrations.AddConstraint(
            model_name='companytag',
            constraint=models.UniqueConstraint(fields=('company', 'language', 'name'), name='unique tag'),
        ),
    ]