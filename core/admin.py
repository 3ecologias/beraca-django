from django.contrib import admin
from .models import *

admin.site.register(Fullwidth_slider_item)

class PortfolioImagesInline(admin.TabularInline):
    model = PortfolioImages
    extra = 3

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [ PortfolioImagesInline, ]

class PostsImagesInline(admin.TabularInline):
    model = BlogImages
    extra = 3

class BlogAdmin(admin.ModelAdmin):
    inlines = [ PostsImagesInline, ]
    save_as = True

class ServiceIconsInline(admin.TabularInline):
    model = ServiceIcons
    extra = 3

class ServiceMethodInline(admin.TabularInline):
    model = ServiceMethod
    extra = 3

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ ServiceIconsInline, ServiceMethodInline, ]

admin.site.register(PortfolioItem, PortfolioAdmin)
admin.site.register(BlogPost, BlogAdmin)
admin.site.register(ServiceItem, ServiceAdmin)
