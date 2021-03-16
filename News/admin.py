from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status')
    list_filter = ('status', )
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(News, NewsAdmin)
