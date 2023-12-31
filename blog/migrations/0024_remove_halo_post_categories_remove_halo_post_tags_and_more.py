# Generated by Django 4.2.1 on 2023-07-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_halo_category_halo_tag_alter_post_tags_halo_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='halo_post',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='halo_post',
            name='tags',
        ),
        migrations.AddField(
            model_name='halo_category',
            name='create_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='halo_category',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='halo_category',
            name='parent_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='halo_category',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='halo_category',
            name='priority',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='halo_category',
            name='slug',
            field=models.CharField(default='1', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='halo_category',
            name='slug_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='halo_category',
            name='thumbnail',
            field=models.CharField(max_length=1023, null=True),
        ),
        migrations.AddField(
            model_name='halo_category',
            name='update_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='create_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='disallow_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='edit_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='editor_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='format_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='likes',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='meta_description',
            field=models.CharField(max_length=1023, null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='meta_keywords',
            field=models.CharField(max_length=511, null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='original_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='slug',
            field=models.CharField(default='1', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='template',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='thumbnail',
            field=models.CharField(max_length=1023, null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='top_priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='update_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='version',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='visits',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='halo_post',
            name='word_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='halo_tag',
            name='color',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='halo_tag',
            name='create_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='halo_tag',
            name='slug',
            field=models.CharField(default='1', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='halo_tag',
            name='slug_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='halo_tag',
            name='thumbnail',
            field=models.CharField(max_length=1023, null=True),
        ),
        migrations.AddField(
            model_name='halo_tag',
            name='update_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='halo_category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='halo_category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='halo_post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='halo_post',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='halo_tag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='halo_tag',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
