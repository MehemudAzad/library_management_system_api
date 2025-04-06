from django.contrib import admin
from .models import Book, Member, BorrowRecord
from django.contrib.auth.admin import UserAdmin


class MemberAdmin(UserAdmin):
    model = Member
    list_display = ('email', 'name', 'phone', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone', 'membershipDate')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

# Register your models here
admin.site.register(Book)
admin.site.register(Member, MemberAdmin)
admin.site.register(BorrowRecord)
