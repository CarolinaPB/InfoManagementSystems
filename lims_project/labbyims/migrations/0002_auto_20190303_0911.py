# Generated by Django 2.1.5 on 2019-03-03 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labbyims', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_used', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='amount used')),
                ('date_used', models.DateField(verbose_name='date of use')),
            ],
        ),
        migrations.RenameField(
            model_name='product_unit',
            old_name='name',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='location',
            name='is_restricted',
        ),
        migrations.RemoveField(
            model_name='location',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product_unit',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='product_unit',
            name='url',
        ),
        migrations.AddField(
            model_name='location',
            name='isbaseliq',
            field=models.BooleanField(default=False, verbose_name='is base liquid'),
        ),
        migrations.AddField(
            model_name='location',
            name='isflammable',
            field=models.BooleanField(default=False, verbose_name='is flammable'),
        ),
        migrations.AddField(
            model_name='location',
            name='isorgminacid',
            field=models.BooleanField(default=False, verbose_name='is organic and mineral acid'),
        ),
        migrations.AddField(
            model_name='location',
            name='isoxidacid',
            field=models.BooleanField(default=False, verbose_name='is oxidizing acid'),
        ),
        migrations.AddField(
            model_name='location',
            name='isoxidliq',
            field=models.BooleanField(default=False, verbose_name='is oxidizing liquid'),
        ),
        migrations.AddField(
            model_name='location',
            name='ispois_vol',
            field=models.BooleanField(default=False, verbose_name='is poison - volatile'),
        ),
        migrations.AddField(
            model_name='location',
            name='ispoison_nonvol',
            field=models.BooleanField(default=False, verbose_name='is poison - non-volatile'),
        ),
        migrations.AddField(
            model_name='location',
            name='isreactive',
            field=models.BooleanField(default=False, verbose_name='is reactive'),
        ),
        migrations.AddField(
            model_name='location',
            name='issolid',
            field=models.BooleanField(default=False, verbose_name='is solid'),
        ),
        migrations.AddField(
            model_name='product',
            name='max_temp',
            field=models.DecimalField(decimal_places=4, default=25, max_digits=10, verbose_name='Minimum Temperature'),
        ),
        migrations.AddField(
            model_name='product',
            name='min_temp',
            field=models.DecimalField(decimal_places=4, default=25, max_digits=10, verbose_name='Maximum Temperature'),
        ),
        migrations.AddField(
            model_name='product_unit',
            name='batch',
            field=models.CharField(blank=True, max_length=255, verbose_name='Batch Number'),
        ),
        migrations.AddField(
            model_name='product_unit',
            name='curr_amount',
            field=models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10, verbose_name='current amount'),
        ),
        migrations.AddField(
            model_name='product_unit',
            name='in_house_no',
            field=models.CharField(blank=True, max_length=255, verbose_name='In House ID'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='cat_num',
            field=models.CharField(blank=True, max_length=255, verbose_name='catalog number'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='exp_date',
            field=models.DateField(blank=True, null=True, verbose_name='expiration date'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='init_amount',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='initial amount'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='is_inactive',
            field=models.BooleanField(default=False, verbose_name='Archived'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='m_unit',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='measuring units'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='open_date',
            field=models.DateField(blank=True, null=True, verbose_name='date opened'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='purity',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='purity/percentage'),
        ),
        migrations.AlterField(
            model_name='product_unit',
            name='ret_date',
            field=models.DateField(blank=True, null=True, verbose_name='retest date'),
        ),
        migrations.AddField(
            model_name='uses',
            name='prod_un',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labbyims.Product_Unit'),
        ),
        migrations.AddField(
            model_name='uses',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
