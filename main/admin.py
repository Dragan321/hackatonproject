from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.models import PaymentItem, Subject, User, UserInfo


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AccountAdmin)
admin.site.register(PaymentItem)
