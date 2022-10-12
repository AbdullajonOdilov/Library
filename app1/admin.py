from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ('ism','id')
    list_display = ('ism','birituvchi','kitob_soni')
    list_display_links = ('ism',)
    list_editable = ('kitob_soni',)
    list_filter = ('birituvchi',)
    list_per_page = 7
    # list_max_show_all =

# @admin.register(Record)
# class RecordAdmin(ModelAdmin):
#     search_fields = ('id','student__ism','kitob__nom')
#     autocomplete_fields = ('student',)

@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    search_fields = ('nom', 'muallif__ism','janr' )
    list_filter = ('janr',)


@admin.register(Record)
class RecordAdmin(ModelAdmin):
    search_fields = ('student__ism','kitob__nom',)
    list_filter = ('qaytardi',)


# @admin.register(Muallif)
# class MuallifAdmin(ModelAdmin):


# admin.site.register(Student)
admin.site.register(Muallif)
# admin.site.register(Kitob)
# admin.site.register(Record)
