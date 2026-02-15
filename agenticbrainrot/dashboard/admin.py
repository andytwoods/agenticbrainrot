from django.contrib import admin

from .models import DatasetAccessGrant


@admin.register(DatasetAccessGrant)
class DatasetAccessGrantAdmin(admin.ModelAdmin):
    list_display = ["user", "email", "granted_by", "granted_at", "reason"]
    list_filter = ["granted_at"]
    search_fields = ["user__email", "email", "reason"]
    raw_id_fields = ["user", "granted_by"]
