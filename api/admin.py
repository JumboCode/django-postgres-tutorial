from django.contrib import admin
from .models import *

class SledAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'victories', 'defeats')

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'sled', 'captain')

# Register your models here.
admin.site.register(Sled, SledAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
