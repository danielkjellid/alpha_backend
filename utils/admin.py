from django.contrib import admin

from utils.models import AuditLog, Note


class AuditLogAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'content_type',
        'object_id',
        'content_object',
        'change',
        'date_of_change'
    ]

admin.site.register(AuditLog, AuditLogAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'content_type',
        'object_id',
        'content_object',
        'note',
        'created_at'
    ]

admin.site.register(Note, NoteAdmin)


  
