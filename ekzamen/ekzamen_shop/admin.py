from django import forms
from django.contrib import admin
from .models import Category, Product, ProductCard
from django.core.urlresolvers import reverse


class CategoryCreatedForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ()


class CategoryCreated(admin.ModelAdmin):
    form = CategoryCreatedForm
    list_display = ('name',)
    search_fields = ('name',)


class ProductCreatedForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()


class ProductsCreated(admin.ModelAdmin):
    form = ProductCreatedForm
    list_display = ('name', 'category',)
    search_fields = ['title', 'price', 'product']

    def get_categorys(self, obj):
        link = reverse('admin:ekzamen_shop_product_change', args=[obj.Category.id])
        return '<a href="{}">{}</a>'.format(link, obj.Category.name)

    get_categorys.admin_order_field = 'name'
    get_categorys.short_description = 'name'
    get_categorys.allow_tags = True


class ProductCardForm(forms.ModelForm):
    class Meta:
        model = ProductCard
        exclude = ()


class ProductCardCreated(admin.ModelAdmin):
    form = ProductCardForm
    list_display = ('product', 'title', 'description', 'price',)
    search_fields = ['title', 'price', 'product']

    # search_fields = ('product', ) and ('title', ) and ('price', )

    def get_categorys(self, obj):
        link = reverse('admin:ekzamen_shop_product_change', args=[obj.product.id])
        return '<a href="{}">{}</a>'.format(link, obj.product.name)

    get_categorys.admin_order_field = 'product__name'
    get_categorys.short_description = 'product name'
    get_categorys.allow_tags = True


admin.site.register(Category, CategoryCreated)
admin.site.register(Product, ProductsCreated)
admin.site.register(ProductCard, ProductCardCreated)
