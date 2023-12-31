# Generated by Django 4.2.1 on 2023-07-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_menu_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='icon',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='target',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.CharField(max_length=1023, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
