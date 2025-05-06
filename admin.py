from django.contrib import admin
from .models import *
from atexit import register

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status', 'created_at')
#     search_fields = ('name',)
#     list_filter = ('status',)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'vendor', 'quantity', 'selling_price', 'status', 'trending')
#     search_fields = ('category',)
#     list_filter = ('category', 'status', 'trending')  # ✅ This shows category as a filter dropdown
#     actions = ['make_trending']

#     def make_trending(self, request, queryset):
#         updated = queryset.update(trending=True)
#         self.message_user(request, f"{updated} products marked as trending.")
#     make_trending.short_description = "Mark selected products as trending"
