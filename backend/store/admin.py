from django.contrib import admin
from store.models import Product, Category, Specification, Gallery, Size, Color


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "category",
        "vendor",
        "price",
        "status",
        "rating",
    ]


# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Specification)
admin.site.register(Gallery)
admin.site.register(Size)
admin.site.register(Color)
