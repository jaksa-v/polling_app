from django.contrib import admin

from .models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class PollAdmin(admin.ModelAdmin):
    list_display = ["question_text"]
    search_fields = ["question_text"]
    fieldsets = [(None, {"fields": ["question_text"]})]
    inlines = [ChoiceInline]


# Register your models here.
admin.site.register(Poll, PollAdmin)
