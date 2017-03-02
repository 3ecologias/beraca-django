from django.contrib import admin
from .models import *

admin.site.register(Fullwidth_slider_item)

class PortfolioImagesInline(admin.TabularInline):
    model = PortfolioImages
    extra = 3

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [ PortfolioImagesInline, ]


admin.site.register(PortfolioItem, PortfolioAdmin)
