from django.contrib import admin

# Register your models here.
from .models import Profile,ChatRel,UserLastSession

admin.site.register((Profile))
@admin.register(ChatRel)
class ChatRel_admin(admin.ModelAdmin):
    list_display = ['chatText','sender','receiver']
    search_fields = ['sender', 'send_time','receiver']
    ordering = ['-send_time']

@admin.register(UserLastSession)
class UserLastSession_admin(admin.ModelAdmin):
    list_display = ['status','lastLogin','user']