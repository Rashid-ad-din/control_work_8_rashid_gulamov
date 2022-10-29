from django.contrib import admin

from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'image')
    list_filter = ('title', 'category')
    search_fields = ('title', 'category')
    fields = ('id', 'title', 'category', 'description', 'image')
    readonly_fields = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'description', 'rating')
    list_filter = ('author', 'product')
    search_fields = ('author', 'product')
    fields = ('id', 'author', 'product', 'description', 'rating')
    readonly_fields = ('id',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
