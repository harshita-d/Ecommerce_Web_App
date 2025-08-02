from django.contrib import admin
from userauths import models


class UserAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email"]
    search_fields = ["full_name", "email"]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["full_name", "country", "gender"]
    search_fields = ["full_name"]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile, ProfileAdmin)
