from django.contrib import admin
from .models import Advertisment 
#from django.utils.html import format_html
#from django.contrib import admin


class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ['title','description','price', 'trades', 'date_now','created_date']
    list_filter = ['date_now', 'description', 'trades']
    fieldsets =(
        ("Первый блок",{
            "fields":("title","description")}),
        ("Второй блок",{
            'classes': ('collapse',),
            "fields":('price','trades')}),
    )
    actions = ['make_true','make_false','created_date']
    @admin.action(description="Обновить торг на True")
    def make_true(self, request, queryset):
        queryset.update(trades = True)

    @admin.action(description="Обновить торг на False")
    def make_false(self, request, queryset):
        queryset.update(trades = False)

admin.site.register(Advertisment,AdvertismentAdmin)