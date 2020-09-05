from django.contrib import admin

# Register your models here.
from .models import Head,Artical_m,Profile,comments,Category

admin.site.register((Head,Artical_m,Profile,comments,Category))

