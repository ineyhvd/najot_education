from django.contrib import admin
from .models import Talaba, Davomat

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ('ism', 'familiya')

@admin.register(Davomat)
class DavomatAdmin(admin.ModelAdmin):
    list_display = ('talaba', 'sana', 'kelgan')
    list_filter = ('sana', 'kelgan')