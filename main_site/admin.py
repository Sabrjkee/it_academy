from django.contrib import admin

from main_site import models as models_ms
from IT import models as models_it


class MoAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(models_ms.MO, MoAdmin)
admin.site.register(models_ms.PhotoMO)
admin.site.register(models_it.MOLocal)
admin.site.register(models_it.EquipmentMO)
admin.site.register(models_it.Equipment)
admin.site.register(models_it.Providers)
admin.site.register(models_it.ProviderMO)


# Register your models here.
