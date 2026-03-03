from django.contrib import admin
from .models import (
    ExpenseTracker,
    Received,
    ReceivedImages,
    Spend,
    SpendImages
)



@admin.register(ExpenseTracker)
class ExpenseTrackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Received)
class ReceivedAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'expensetracker',
        'sr_no',
        'date',
        'received_from',
        'description',
        'amount'
    )


@admin.register(ReceivedImages)
class ReceivedImagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'received',
        'image'
    )



@admin.register(Spend)
class SpendAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'expensetracker',
        'sr_no',
        'date',
        'sent_to',
        'description',
        'amount'
    )



@admin.register(SpendImages)
class SpendImagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'spend',
        'image'
    )