from django import forms
from django.contrib import admin
from .models import Category,Product
from django.core.urlresolvers import reverse
from ckeditor.widgets import CKEditorWidget


class CategoryCreatedForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ()


class CategoryCreated(admin.ModelAdmin):
    form = CategoryCreatedForm
    list_display = ('name', 'created_at', 'updated_at', )
    readonly_fields = ('updated_at', 'created_at', )


class ProductCreatedForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ()


class ProductCreated(admin.ModelAdmin):
    form = ProductCreatedForm
    list_display = ('name', 'price', 'description', 'cover', 'in_stock', 'categorys', )

    def get_news(self,obj):
        link = reverse('admin:main_app_product_change', args=[obj.product.id])
        return '<a href="{}">{}</a>'.format(link, obj.product.name)
    get_news.admin_order_field = 'product__name' # поле по которому происходит сортировка
    get_news.short_description = 'Product name'
    get_news.allow_tags = True # включает нам теги

"""
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'get_news', 'content', 'created_at', )
"""


admin.site.register(Category, CategoryCreated)
admin.site.register(Product, ProductCreated)