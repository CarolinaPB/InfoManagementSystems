# Generated by Django 2.1.6 on 2019-02-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labbyims', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_unit',
            old_name='name',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='product_unit',
            name='url',
        ),
        migrations.AddField(
            model_name='product_unit',
            name='m_unit',
            field=models.CharField(blank=True, max_length=4, verbose_name='measuring units'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='cat_num',
            field=models.CharField(blank=True, max_length=255, verbose_name='catalog number'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='exp_date',
            field=models.DateField(blank=True, verbose_name='expiration date'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='is_inactive',
            field=models.BooleanField(default=False, verbose_name='Archived'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='open_date',
            field=models.DateField(blank=True, verbose_name='date opened'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='purity',
            field=models.CharField(blank=True, max_length=255, verbose_name='purity/percentage'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='ret_date',
            field=models.DateField(blank=True, verbose_name='retest date'),
        ),
    ]