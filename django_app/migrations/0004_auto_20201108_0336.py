# Generated by Django 3.1.2 on 2020-11-08 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_auto_20201106_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='log',
            new_name='lon',
        ),
        migrations.RemoveField(
            model_name='home',
            name='bath',
        ),
        migrations.RemoveField(
            model_name='home',
            name='bed',
        ),
        migrations.RemoveField(
            model_name='home',
            name='lat_long',
        ),
        migrations.RemoveField(
            model_name='home',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='home',
            name='street',
        ),
        migrations.RemoveField(
            model_name='home',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='home',
            name='abbreviation',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='baths',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='baths_full',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='beds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='fips_code',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='href',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='line',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='listing_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='mls_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='neighborhood_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='page_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='photo_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='postal_code',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='prop_status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='prop_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='property_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='rank',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='rdc_web_url',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='state_code',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='thumbnail',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='units',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='city',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='state',
            field=models.CharField(max_length=15, null=True),
        ),
    ]