# Generated by Django 4.2.1 on 2023-07-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_menu_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={},
        ),
        migrations.AddField(
            model_name='menu',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
