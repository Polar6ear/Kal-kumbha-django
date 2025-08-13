from django.contrib import admin
from .models import Account, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined', )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

    def thumbnail(self, obj):
        if obj.profile_picture and hasattr(obj.profile_picture, 'url'):
            return format_html('<img src="{}" width="30" style="border-radius:50%;">', obj.profile_picture.url)
        return "(No Image)"

    thumbnail.short_description = 'Profile Picture'

admin.site.register(UserProfile, UserProfileAdmin)
