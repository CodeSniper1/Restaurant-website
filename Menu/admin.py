from django.contrib import admin
from Menu.models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display=('name','description','price','image','availabilityTime')
    
    
admin.site.register(Menu,MenuAdmin)    

