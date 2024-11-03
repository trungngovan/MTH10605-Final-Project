from django.contrib import admin
from .models import (
    Keyword,
    Result,
)

@admin.register(Keyword)
class KeyWordAdmin(admin.ModelAdmin):
    """UI for KeyWord model."""
    list_display = (
        "id",
        "word",
        "type",
        "score",
    )
    search_fields = (
        "word",
    )
    list_filter = (
        "type",
    )
    readonly_fields = (
        "created",
        "modified",
    )


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    """UI for Result model."""
    list_display = (
        "id",
        "type",
        "score",
    )
    list_filter = (
        "type",
    )
    readonly_fields = (
        "created",
        "modified",
    )
