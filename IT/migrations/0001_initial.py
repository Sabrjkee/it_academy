# Generated by Django 2.1.3 on 2018-12-18 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentMO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_number', models.CharField(max_length=255)),
                ('statick_ip', models.BooleanField(default=False)),
                ('ip_adress', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('include_web_interface', models.BooleanField(default=False)),
                ('lan_name', models.CharField(blank=True, max_length=255, null=True)),
                ('login_for_web', models.CharField(blank=True, max_length=255, null=True)),
                ('pass_for_web', models.CharField(blank=True, max_length=255, null=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='MOLocal',
            fields=[
                ('mo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main_site.MO')),
                ('first_ip_adress', models.GenericIPAddressField(protocol='IPv4')),
                ('getway', models.GenericIPAddressField(protocol='IPv4')),
                ('static_ip', models.GenericIPAddressField(protocol='IPv4')),
                ('mask', models.GenericIPAddressField(protocol='IPv4')),
            ],
        ),
        migrations.CreateModel(
            name='ProviderMO',
            fields=[
                ('mo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main_site.MO')),
                ('number_of_contract', models.CharField(max_length=255)),
                ('date_of_contract', models.DateField()),
                ('provider_equipment', models.BooleanField()),
                ('provider_eq_type', models.CharField(max_length=255)),
                ('provider_eq_settings', models.CharField(choices=[('BR', 'Bridge'), ('PM', 'Port Mapping')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ur_adress', models.CharField(max_length=255)),
                ('provider_phone_number', models.CharField(max_length=255)),
                ('urls_to_web', models.URLField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='providermo',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT.Providers'),
        ),
        migrations.AddField(
            model_name='equipmentmo',
            name='mo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.MO'),
        ),
    ]