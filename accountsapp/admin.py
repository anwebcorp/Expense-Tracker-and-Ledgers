from django.contrib import admin
from .models import Business, Ledgers, MaineDiye, ManineDiyeImages, MaineLiye


class ManineDiyeImagesInline(admin.TabularInline):
    model = ManineDiyeImages
    extra = 1


class MaineDiyeAdmin(admin.ModelAdmin):
    inlines = [ManineDiyeImagesInline]

    list_display = ('ledger', 'sr_no', 'date', 'description', 'maine_diye')
    search_fields = ('sr_no', 'ledger__cutomer_name', 'description')
    list_filter = ('date',)


class MaineLiyeAdmin(admin.ModelAdmin):
    list_display = ('ledger', 'sr_no', 'date', 'description', 'maine_liye')
    search_fields = ('sr_no', 'ledger__cutomer_name', 'description')
    list_filter = ('date',)


class LedgersAdmin(admin.ModelAdmin):
    list_display = ('business', 'cutomer_name')
    search_fields = ('cutomer_name',)


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('bus_name',)


admin.site.register(MaineDiye, MaineDiyeAdmin)
admin.site.register(MaineLiye, MaineLiyeAdmin)
admin.site.register(Ledgers, LedgersAdmin)
admin.site.register(Business, BusinessAdmin)