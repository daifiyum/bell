# Generated by Django 4.2.1 on 2023-07-07 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_remove_halo_post_categories_remove_halo_post_tags_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Halo_Category',
        ),
        migrations.DeleteModel(
            name='Halo_Post',
        ),
        migrations.DeleteModel(
            name='Halo_Tag',
        ),
    ]