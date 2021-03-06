

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('user', models.ManyToManyField(through='labbyims.Association', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('temperature', models.DecimalField(decimal_places=4, default=25, max_digits=10, verbose_name='Temperature')),
                ('description', models.TextField(blank=True)),
                ('ispoison_nonvol', models.BooleanField(default=False, verbose_name='poison - non-volatile')),
                ('ispois_vol', models.BooleanField(default=False, verbose_name='poison - volatile')),
                ('isreactive', models.BooleanField(default=False, verbose_name='reactive')),
                ('issolid', models.BooleanField(default=False, verbose_name='solid')),
                ('isbaseliq', models.BooleanField(default=False, verbose_name='base liquid')),
                ('isoxidliq', models.BooleanField(default=False, verbose_name='oxidizing liquid')),
                ('isoxidacid', models.BooleanField(default=False, verbose_name='oxidizing acid')),
                ('isorgminacid', models.BooleanField(default=False, verbose_name='organic and mineral acid')),
                ('isflammable', models.BooleanField(default=False, verbose_name='flammable')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cas', models.CharField(max_length=12, unique=True, verbose_name='CAS number')),
                ('name', models.CharField(max_length=255)),
                ('min_temp', models.DecimalField(decimal_places=3, default=25, max_digits=6, verbose_name='Maximum Temperature')),
                ('max_temp', models.DecimalField(decimal_places=3, default=25, max_digits=6, verbose_name='Minimum Temperature')),
                ('ispoison_nonvol', models.BooleanField(verbose_name='poison - non-volatile')),
                ('isreactive', models.BooleanField(verbose_name='reactive')),
                ('issolid', models.BooleanField(verbose_name='solid')),
                ('isoxidliq', models.BooleanField(verbose_name='oxidizing liquid')),
                ('isflammable', models.BooleanField(verbose_name='flammable')),
                ('isbaseliq', models.BooleanField(verbose_name='base liquid')),
                ('isorgminacid', models.BooleanField(verbose_name='organic and mineral acid')),
                ('isoxidacid', models.BooleanField(verbose_name='oxidizing acid')),
                ('ispois_vol', models.BooleanField(verbose_name='poison - volatile')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_house_no', models.CharField(blank=True, max_length=255, verbose_name='In House ID')),
                ('del_date', models.DateField(verbose_name='delivery date')),
                ('company', models.CharField(max_length=255)),
                ('cat_num', models.CharField(blank=True, max_length=255, verbose_name='catalog number')),
                ('description', models.CharField(max_length=255)),
                ('batch', models.CharField(blank=True, max_length=255, verbose_name='Batch Number')),
                ('init_amount', models.DecimalField(decimal_places=4, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='initial amount')),
                ('m_unit', models.CharField(blank=True, max_length=4, null=True, verbose_name='measuring units')),
                ('purity', models.CharField(blank=True, max_length=255, null=True, verbose_name='purity/percentage')),
                ('exp_date', models.DateField(blank=True, null=True, verbose_name='expiration date')),
                ('ret_date', models.DateField(blank=True, null=True, verbose_name='retest date')),
                ('open_date', models.DateField(blank=True, null=True, verbose_name='date opened')),
                ('used_amount', models.DecimalField(decimal_places=4, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='amount used')),
                ('is_inactive', models.BooleanField(default=False, verbose_name='Archived')),
                ('curr_amount', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='current amount')),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_res', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Amount to Reserve')),
                ('date_res', models.DateField(verbose_name='Reservation Date')),
                ('is_complete', models.BooleanField(null=True)),
                ('res_name', models.CharField(default='Reservation', max_length=255, unique=True, verbose_name='Reservation Name')),
                ('prod_un', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labbyims.Product_Unit', verbose_name='description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=255)),
                ('building_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Uses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_used', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='amount used')),
                ('date_used', models.DateField(verbose_name='date of use')),
                ('prod_un', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labbyims.Product_Unit', verbose_name='description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_warn', models.BooleanField(verbose_name='Running Low Warning')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labbyims.Department')),
                ('prod_un', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labbyims.Product_Unit')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product_unit',
            name='department',
            field=models.ManyToManyField(blank=True, default=None, through='labbyims.Watching', to='labbyims.Department'),
        ),
        migrations.AddField(
            model_name='product_unit',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labbyims.Location'),
        ),
        migrations.AddField(
            model_name='product_unit',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labbyims.Product'),
        ),
        migrations.AddField(
            model_name='product_unit',
            name='reservation',
            field=models.ManyToManyField(through='labbyims.Reserve', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='location',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labbyims.Room'),
        ),
        migrations.AddField(
            model_name='association',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labbyims.Department', verbose_name='department'),
        ),
        migrations.AddField(
            model_name='association',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='association',
            unique_together={('user', 'dept')},
        ),
    ]
