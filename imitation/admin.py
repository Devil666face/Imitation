from django.contrib import admin
from imitation.models import (
    Incident,
    Category,
    ExampleIncident,
)


class IncidentAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'legal',]
    search_fields = ['title',]
    list_display = ['title', 'created_at', 'category', 'legal', ]
    list_filter = ['created_at', 'category', 'legal']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', ]
    list_display = ['title', ]
    search_fields = ['title', ]


class ExpamleIncidentAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'legal', ]
    search_fields = ['title',]
    list_display = ['title', 'category', 'legal', ]
    list_filter = ['category', 'legal']
    list_editable = ['category', 'legal']


admin.site.register(Incident, IncidentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ExampleIncident, ExpamleIncidentAdmin)
