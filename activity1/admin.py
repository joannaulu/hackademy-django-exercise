from django.contrib import admin
from .models import Profile

# Register your models here.
admin.site.site_header = "Joanna's Admin Page"


class ProfileAdmin(admin.ModelAdmin):
    #list_display = ('user', 'description',)
    list_display = ('user', 'get_first_name', 'get_last_name', 'description')

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = "First Name"

    @admin.display(ordering='user__last_name', description='Last Name')
    def get_last_name(self, obj):
        return obj.user.last_name


    def has_delete_permission(self, request, obj=None) :
        return False
    
    def has_add_permission(self, request, obj=None) :
        return False

admin.site.register(Profile, ProfileAdmin)


