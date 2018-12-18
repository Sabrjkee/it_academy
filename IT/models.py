from django.db import models
from main_site import models as models_main


class MOLocal (models.Model):
    mo = models.OneToOneField(
        models_main.MO,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_ip_adress = models.GenericIPAddressField(
        protocol='IPv4'
    )
    getway = models.GenericIPAddressField(
        protocol='IPv4'
    )
    static_ip = models.GenericIPAddressField(
        protocol='IPv4'
    )
    mask = models.GenericIPAddressField(
        protocol='IPv4'
    )


class Equipment(models.Model):
    name = models.CharField(
        max_length=255
    )
    model = models.CharField(
        max_length=255
    )


class EquipmentMO (models.Model):
    mo = models.ForeignKey(
        models_main.MO,
        on_delete=models.CASCADE,
    )
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE
    )
    inventory_number = models.CharField(
        max_length=255
    )
    statick_ip = models.BooleanField(
        default=False
    )
    ip_adress = models.GenericIPAddressField(
        protocol='IPv4',
        null=True,
        blank=True,
    )
    include_web_interface = models.BooleanField(
        default=False
    )
    lan_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    login_for_web = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    pass_for_web = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )


class Providers(models.Model):
    name = models.CharField(
        max_length=255
    )
    ur_adress = models.CharField(
        max_length=255
    )
    provider_phone_number = models.CharField(
        max_length=255
    )
    urls_to_web = models.URLField(
        max_length=255,
        null=True,
        blank=True,
    )


class ProviderMO (models.Model):
    mo = models.OneToOneField(
        models_main.MO,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    number_of_contract = models.CharField(
        max_length=255
    )
    date_of_contract = models.DateField()
    provider_equipment = models.BooleanField()
    provider_eq_type = models.CharField(
        max_length=255
    )
    provider_eq_settings = models.CharField(
        max_length=2,
        choices=[('BR', 'Bridge'), ('PM', 'Port Mapping')]
    )
    provider = models.ForeignKey(
        Providers,
        on_delete=models.CASCADE
    )
