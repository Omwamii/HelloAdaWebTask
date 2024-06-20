from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',) # avoid change of field on update

admin.site.register(Task, TaskAdmin)