from django.contrib import admin

# Register your models here.
from .models import Hotel
from .models import reviewer
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class HotelResource(resources.ModelResource):
    class Meta:
        model = Hotel

class ReviewerResource(resources.ModelResource):
    class Meta:
        model = reviewer


class HotelAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = HotelResource
    list_display = ('nama','harga','kota','alamat')
    ordering = ('-timestamp',) 

class ReviewAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = ReviewerResource
    list_display = ('ratinghotel','rating','date','review')
    ordering = ('-date',) 


admin.site.register(Hotel,HotelAdmin)
admin.site.register(reviewer,ReviewAdmin)