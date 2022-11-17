from myapp.models import Product
from django.contrib import admin

# Register your models here.
# admin.site.register(Product)

# To modify django admin panell

admin.site.site_header = 'Openkart Cart Administration'
admin.site.site_title = 'Openkart'
admin.site.index_title ='Openkart Cart'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','id','price','description')
    search_fields = ('name',)
    
    def set_price_to_zero(self,request,queryset):
        queryset.update(price=0)
        
    def set_price_to_fiftyk(self,request,queryset):
        queryset.update(price=50000)
        
    action = ('set_price_to_zero','set_price_to_fiftyk',)
    
admin.site.register(Product,ProductAdmin)
