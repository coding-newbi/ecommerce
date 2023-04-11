from django.contrib import admin

from shopapp.models import Category1, Product1


# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category1,categoryadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','update']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product1,productadmin)

