from django.contrib import admin
from .models import SsqInfo, SsqOrig

# Register your models here.


@admin.register(SsqInfo)
class SsqInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(SsqOrig)
class SsqOrigAdmin(admin.ModelAdmin):
    pass


# admin.site.register(SsqOrig, SsqOrigAdmin)
# admin.site.register(SsqInfo, SsqInfoAdmin)
