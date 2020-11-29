from django.contrib import admin

# Register your models here.
from .models import Head,Artical_m,comments,Category

admin.site.register((Head,comments,Category))

@admin.register(Artical_m)
class Artical_admin(admin.ModelAdmin):
    list_display=('title','said','slug','In_image','categories','creater')
    search_fields = ('title','said')
    ordering=('status','create_date')

